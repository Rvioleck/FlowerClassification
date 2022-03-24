import shutil

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap

from AIModel.cnn_models import *
from AIModel.data_process import *
from custom_widget.notification import NotificationWindow


class AIModelOperationThread(QThread):
    """
    AI操作线程
    """

    flower_words = ["azalea", "bougainvillea", "camellia", "carnation", "chrysanthemum", "daisy",
                    "dandelion", "fragrans", "gardenia", "hibiscus", "hydrangea", "iris",
                    "lilac", "lily", "lotus", "morningglory", "narcissus", "peachflower",
                    "peony", "phalaenopsis", "rose", "sakura", "sunflower", "tulip"]

    load_signal = Signal(Model)
    load_failed_signal = Signal()
    preload_signal = Signal(Model)
    batch_classify_res_signal = Signal(int, str, bool)
    batch_classify_finish_signal = Signal()
    # 传递结果列表portion, 结果值res, 是否为深度测评tag
    classify_res_signal = Signal(list, str, bool)
    deep_classify_finish = Signal()

    def __init__(self, window=None, parent=None):
        super(AIModelOperationThread, self).__init__(parent)
        self.operation = "load"
        self.ai_model = EfficientNetB0()
        self.window = window
        self.files = None

    def run(self) -> None:
        if self.operation == "load":  # 线程进行模型加载
            self.__load()  # 加载AI模型
            # self.preClassify()  # 预加载模型权重
        elif self.operation == "preClassify":
            self.__preClassify()
        elif self.operation == "classify":
            self.__classify()
        elif self.operation == "batchClassify":
            self.__batchClassify()
        elif self.operation == "deepClassify":
            self.__deepClassify()
        elif self.operation == "batchExport":
            self.__batchExport()

    def __classify(self):
        # self.files仅含一个元素
        x = get_input_x(self.files)
        portion, index = model_predict(self.ai_model, x)
        res = self.flower_words[index]
        self.classify_res_signal[list, str, bool].emit(portion, res, False)
        print("AI Thread has finished classifying")

    def __batchClassify(self):
        for i, file in enumerate(self.files):
            x = get_input_x(QPixmap(file))
            portion, index = model_predict(self.ai_model, x)
            res = self.flower_words[index]
            self.batch_classify_res_signal[int, str, bool].emit(i, res, False)
        self.batch_classify_finish_signal[None].emit()
        print("AI Thread has finished batchClassifying")

    def __deepClassify(self):
        model_weight = {
            "EfficientNetB0": 0.956, "EfficientNetB2": 0.952, "EfficientNetB4": 0.947, "EfficientNetB7": 0.959,
            "MobileNetV2": 0.927, "DenseNet121": 0.909, "InceptionV3": 0.898, "VGG19": 0.707
        }
        whole_portion = [0] * len(self.flower_words)
        cur_model_name = self.ai_model.__class__.__name__
        x = get_input_x(self.files)
        portion, index = model_predict(self.ai_model, x)
        self.__calPortion(portion, whole_portion, model_weight, cur_model_name)
        for model_name, weight in model_weight.items():
            if model_name == cur_model_name:
                continue
            model = eval(model_name + "()")
            load_success = load_model(model)
            if not load_success:
                continue
            portion, index = model_predict(model, x)
            self.__calPortion(portion, whole_portion, model_weight, model_name)
        self.deep_classify_finish[None].emit()
        print("AI Thread has finished deepClassifying")

    def __batchExport(self):
        path = self.window.savePathLineEdit.text()
        count = self.window.tableWidget.rowCount()
        exported_flag = False  # 布尔变量用于记录此次是否进行过导出
        for i in range(count):
            self.batch_classify_res_signal[int, str, bool].emit(i, None, True)
            src_path = self.window.files[i]
            file_name = self.window.tableWidget.item(i, 1).text()
            if self.window.tableWidget.item(i, 2) is None:  # 空项跳过
                continue
            kind_prediction = self.window.tableWidget.item(i, 2).text()
            if kind_prediction == "":  # 无预测结果的项跳过
                continue
            exported_flag = True
            if self.window.batchRenameCheckBox.isChecked():
                # 开启批量重命名
                file_type = file_name.split(".")[-1]
                file_name = kind_prediction + "." + file_type
            dir_path = path + "/" + kind_prediction
            save_path = dir_path + "/" + file_name  # 保存文件路径名：flower.jpg
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            i = 1
            des_path = save_path  # 复制文件路径名：flower (3).jpg
            while os.path.isfile(des_path):
                # 判断是否有重名文件，避免覆盖
                prefix, postfix = save_path.split(".")
                des_path = "{} ({}).{}".format(prefix, i, postfix)
                i += 1
            shutil.copy(src_path, des_path)  # 从源地址复制到目的地址
            height, width = self.window.spinBox_height_2.value(), self.window.spinBox_width_2.value()
            if self.window.convertModeCheckBox.isChecked():  # 选择批量更改色彩模式
                img = Image.open(des_path)
                img = img.convert("RGB")
                if height != 0 and width != 0:  # 选择批量更改分辨率
                    img = img.resize((height, width), Image.ANTIALIAS)
                os.remove(des_path)
                des_path = des_path.split(".")[0] + ".jpg"
                while os.path.isfile(des_path):
                    # 判断是否有重名文件，避免覆盖
                    prefix, postfix = save_path.split(".")
                    des_path = "{} ({}).{}".format(prefix, i, postfix)
                    i += 1
                img.save(des_path)
            else:  # 未选择批量更改色彩模式
                if height != 0 and width != 0:  # 选择批量更改分辨率
                    img = Image.open(des_path)
                    img = img.resize((height, width), Image.ANTIALIAS)
                    img.save(des_path)
        if not exported_flag:
            # 此次未经过导出
            NotificationWindow.info(self.window, "注意", "请先进行图片预测")
            # QMessageBox.information("注意", "请先进行图片预测", QMessageBox.Ok)
        else:
            os.startfile(path)
        self.window._release_button()

    def __calPortion(self, portion, whole_portion, model_weight, model_name):
        for i, per in enumerate(portion):
            whole_portion[i] += per * model_weight[model_name]
        res = self.flower_words[whole_portion.index(max(whole_portion))]
        standard_portion = [(i / sum(whole_portion)) for i in whole_portion]
        self.classify_res_signal[list, str, bool].emit(standard_portion, res, True)

    def __load(self):
        # AI线程进行模型初始化操作
        load_success = load_model(self.ai_model)
        if not load_success:
            self.load_failed_signal[None].emit()
        else:
            self.load_signal[Model].emit(self.ai_model)
        print("AI Thread has finished loading")

    def __preClassify(self):
        # AI线程参数预加载操作
        x = get_input_x(QPixmap("images/帮助.png"))
        model_predict(self.ai_model, x)
        self.preload_signal[Model].emit(self.ai_model)
        print("AI Thread has finished preClassifying")

    def setOperation(self, operation: str):
        self.operation = operation

    def setModel(self, model: Model):
        self.ai_model = model

    def setFiles(self, files):
        self.files = files
