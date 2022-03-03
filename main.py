import shutil
import sys

from PIL import ImageGrab
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtCore import QEvent, QPoint, QThread, Signal, QSize
from PySide6.QtGui import QAction, QPen, Qt, QPainter, QIcon, QColor, QCursor, QKeySequence, QShortcut, QFont
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication, QTableWidgetItem, QMenu, QToolButton, \
    QToolTip

from AIModel.cnn_models import *
from AIModel.data_process import *
from ImageCutter import Form
from ImageViewer import ImageViewer
from ui_MainWindowFlower import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        # AI线程初始化
        self.AIThread = AIModelOperationThread()
        self.AIThread.load_signal[Model].connect(self.loadModel)  # 加载模型
        self.AIThread.preload_signal[Model].connect(self.preLoadModel)
        self.AIThread.load_failed_signal[None].connect(self.loadFailed)
        self.AIThread.classify_res_signal[int, str].connect(self.setClassifyRes)
        self.AIThread.start()
        # 全局变量初始化
        self.flower_path = ""
        self.flower_image = None
        self.batchDirectory = ""  # 记录批量图片保存路径
        self.flowers = ["叶子花", "雏  菊", "蒲公英", "栀子花", "木槿花", "绣球花",
                        "鸢尾花", "百合花", "荷  花", "牵牛花", "桃  花", "牡丹花",
                        "蝴蝶兰", "玫瑰花", "向日葵", "郁金香"]
        self.flower_words = ["bougainvillea", "daisy", "dandelion", "gardenia", "hibiscus", "hydrangea",
                             "iris", "lily", "lotus", "morningglory", "peachflower", "peony", "phalaenopsis",
                             "rose", "sunflower", "tulip"]
        self.files = []  # 记录已选中的批量图片路径
        self.setupUi(self)  # GUI界面初始化(Viewer)
        self.initUI()  # 业务操作初始化(Controller)

    def initUI(self):
        # 绑定按钮点击信号
        self.chooseButton.clicked.connect(self.getImage)
        self.batchChooseButton.clicked.connect(self.getBatchImage)
        self.predictButton.clicked.connect(self.classifyImage)
        self.clearTableButton.clicked.connect(self.clearTableContent)
        self.batchPredictButton.clicked.connect(self.classifyBatchImages)
        self.getDirectoryButton.clicked.connect(self.getBatchDirectory)
        self.batchExportButton.clicked.connect(self.exportBatchImages)
        self.cutButton.clicked.connect(self.cutImage)
        self.resetButton.clicked.connect(self.resetImage)
        self.saveButton.clicked.connect(self.saveImage)

        # 事件过滤器
        self.imageLabel.installEventFilter(self)
        # 绑定工具栏触发信号
        self.toolBar.actionTriggered[QAction].connect(self.chooseModel)
        # 绑定菜单栏触发信号
        self.menu.triggered[QAction].connect(self.menuOperation)
        # 绑定表格组件点击信号
        self.tableWidget.cellDoubleClicked.connect(self.viewImage)
        # 绑定表格组件右键菜单信号
        self.tableWidget.customContextMenuRequested.connect(self.popMenu)

        # 定义tableWidget的右键菜单栏
        self.twPopMenu = QMenu()  # tableWidget右键菜单
        self.delAction = QAction(QIcon("./images/删除.png"), "删除")  # tableWidget删除行为
        self.twPopMenu.addAction(self.delAction)  # 行为添加至菜单
        self.delAction.triggered.connect(self.deleteRow)  # 绑定"删除行为"的槽
        # label预加载
        self.batchImportLabel.setText("已加载图片张数：0张")
        self.statusBar().showMessage("正在加载模型中...")
        self.resultLabel.setText("未导入图片")
        # 应用程序全局热键
        QShortcut(QKeySequence(self.tr("Ctrl+V")), self, self.pasteImage)
        # 预测详细信息按钮
        self.detailToolButton = QToolButton()
        self.detailToolButton.setObjectName(u"detailToolButton")
        icon10 = QIcon()
        icon10.addFile(u"images/\u5e2e\u52a9.png", QSize(), QIcon.Normal, QIcon.Off)
        self.detailToolButton.setIcon(icon10)
        self.detailToolButton.setIconSize(QSize(20, 20))
        self.detailToolButton.setAutoRaise(True)

    def eventFilter(self, watched, event) -> bool:
        """过滤器实现label点击事件"""
        if watched == self.imageLabel:
            if event.type() == QEvent.MouseButtonDblClick:
                self.getImage()
        # 对于其余情况返回默认处理方法
        return QMainWindow.eventFilter(self, watched, event)

    def loadModel(self, model):
        # AI模型初始化(Model)
        self.ai_model = model
        QMessageBox.information(self, "成功",
                                "成功导入模型" + self.ai_model.__class__.__name__,
                                QMessageBox.Ok)
        self.statusBar().showMessage("模型：" + self.ai_model.__class__.__name__)

    def preLoadModel(self, model):
        # AI模型预加载
        self.ai_model = model
        print("Main Thread Model id:{}".format(id(self.ai_model)))

    def loadFailed(self):
        QMessageBox.warning(self, "错误", "未导入该模型！", QMessageBox.Ok)

    def chooseModel(self, model_action):
        if model_action == self.actionCNN:
            self._showStatistics()
            return
        if model_action == self.myModelAction:
            self.AIThread.setModel(MyModel())
        elif model_action == self.denseNet121Action:
            self.AIThread.setModel(DenseNet121())
        elif model_action == self.efficientNetB0Action:
            self.AIThread.setModel(EfficientNetB0())
        elif model_action == self.efficientNetB4Action:
            self.AIThread.setModel(EfficientNetB4())
        elif model_action == self.efficientNetB7Action:
            self.AIThread.setModel(EfficientNetB7())
        elif model_action == self.inceptionAction:
            self.AIThread.setModel(InceptionV3())
        elif model_action == self.vggAction:
            self.AIThread.setModel(VGG19())
        elif model_action == self.mobileNetAction:
            self.AIThread.setModel(MobileNetV2())
        # AI线程启动模型加载
        print("AI Thread is running: load")
        self.AIThread.setOperation("load")
        self.AIThread.start()

    def getBatchDirectory(self):
        # 选取文件夹
        self.batchDirectory = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                               "D:\\AI_LEARNING_PDF\\deep learning\\flower_images")
        self.savePathLineEdit.setText(self.batchDirectory)

    def getBatchImage(self):
        # AI线程启动参数预加载
        print("AI Thread is running: preClassify")
        self.AIThread.setOperation("preClassify")
        self.AIThread.start()
        try:
            # 获取选择图片
            files, _ = QFileDialog.getOpenFileNames(self, "Open files",
                                                    "D:\\AI_LEARNING_PDF\\deep learning\\flower_images",
                                                    "Image Files (*.jpg *.png *.jpeg *.gif)")
            row_count = self.tableWidget.rowCount()  # 统计原本数量
            for i, file in enumerate(files):
                # 遍历此次所选图片，加入表格项
                img_path, img_name = os.path.split(file)  # 分割路径和图片名
                self.tableWidget.insertRow(row_count + i)  # 在原有基础上添加项
                self.tableWidget.setItem(row_count + i, 0, QTableWidgetItem(img_path))
                self.tableWidget.setItem(row_count + i, 1, QTableWidgetItem(img_name))
                self.tableWidget.setItem(row_count + i, 2, QTableWidgetItem(""))
            self.files.extend(files)  # 累计已导入文件
            self.batchImportLabel.setText("已加载图片张数：{}".format(len(self.files)))
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "警告", "请选择一个有效路径", QMessageBox.Ok)

    def classifyBatchImages(self):
        # AI线程启动批量预测
        print("AI Thread is running: classify")
        self.AIThread.setFiles(self.files)
        self.AIThread.setOperation("classify")
        self.AIThread.start()

    def setClassifyRes(self, i, res):
        icon_path = u"images/flowers/{}.png".format(res)
        self.tableWidget.setItem(i, 2, QTableWidgetItem(QIcon(icon_path), res))

    def clearTableContent(self):
        res = QMessageBox.information(self, "确认", "是否清除已导入图片",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.tableWidget.setRowCount(0)
            self.tableWidget.clearContents()
            self.files.clear()
            self.batchImportLabel.setText("已加载图片张数：{}".format(len(self.files)))

    def popMenu(self, point: QPoint):
        try:
            item = self.tableWidget.itemAt(point)
            self.delete_row_num = item.row()
            # 绑定删除事件的信号
            self.twPopMenu.exec(QCursor().pos())
        except Exception as e:
            print(e)
            self.delete_row_num = -1  # 置为无效值

    def deleteRow(self):
        try:
            row_num = self.delete_row_num
            self.tableWidget.removeRow(row_num)
            self.files.pop(row_num)
            self.batchImportLabel.setText("已加载图片张数：{}".format(len(self.files)))
        except Exception as e:
            print(e)

    def exportBatchImages(self):
        path = self.savePathLineEdit.text()
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except FileNotFoundError:
            QMessageBox.information(self, "注意", "请先选择导出路径", QMessageBox.Ok)
            return
        count = self.tableWidget.rowCount()
        if count == 0:
            QMessageBox.information(self, "注意", "请先导入图片进行图片预测", QMessageBox.Ok)
            return
        exported_flag = False  # 布尔变量用于记录此次是否进行过导出
        for i in range(count):
            src_path = self.files[i]
            file_name = self.tableWidget.item(i, 1).text()
            if self.tableWidget.item(i, 2) is None:  # 空项跳过
                continue
            kind_prediction = self.tableWidget.item(i, 2).text()
            if kind_prediction == "":  # 无预测结果的项跳过
                continue
            if self.batchRenameRadioButton.isChecked():
                # 开启批量重命名
                file_type = file_name.split(".")[-1]
                file_name = kind_prediction + "." + file_type
            dir_path = path + "/" + kind_prediction
            save_path = dir_path + "/" + file_name  # 保存文件路径名：flower.jpg
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            exported_flag = True
            i = 1
            des_path = save_path  # 复制文件路径名：flower (3).jpg
            while os.path.isfile(des_path):
                # 判断是否有重名文件，避免覆盖
                prefix, postfix = save_path.split(".")
                des_path = "{} ({}).{}".format(prefix, i, postfix)
                i += 1
            shutil.copy(src_path, des_path)  # 从源地址复制到目的地址
        if not exported_flag:
            # 此次未经过导出
            QMessageBox.information(self, "注意", "请先进行图片预测", QMessageBox.Ok)
        else:
            os.startfile(path)

    def saveImage(self):
        if self.flower_path == "":  # 未导入图片则不进入函数
            return
        save_directory = QFileDialog.getExistingDirectory(self, "选取保存文件夹",
                                                          "D:\\AI_LEARNING_PDF\\deep learning\\flower_images")
        if save_directory == "":  # 未选择文件夹则退出函数
            return
        save_path = save_directory + "/" + self.flower_name  # 拼接保存路径：文件夹+文件原始名称
        self.flower_image.save(save_path)
        answer = QMessageBox.information(self, "保存成功",
                                         "文件路径为：{}".format(save_path), QMessageBox.Open | QMessageBox.Ok)
        if answer == QMessageBox.Open:
            os.startfile(save_path)

    def passImage(self, pixmap):
        self.imageLabel.setPixmap(pixmap)
        self.flower_pixmap = pixmap
        self.flower_image = ImageQt.fromqpixmap(pixmap)
        self.imageTextEdit.setText(
            "<p>图片分辨率：<b><font color=red>{}×{}</font></b></p>"
            "<p>图片格式：<b><font color=red>{}</font></b></p>"
            "<p>色彩模式：<b><font color=red>{}</font></b></p>".format(
                self.flower_image.size[0], self.flower_image.size[1], self.flower_image.format, self.flower_image.mode))

    def cutImage(self):
        self.image_cutter = Form(image=self.flower_pixmap)
        self.image_cutter.save_signal.connect(self.passImage)
        self.image_cutter.show()

    def viewImage(self, row):
        print(self.files[row])
        self.image_viewer = ImageViewer(image=self.files[row], background=QColor(28, 31, 34))
        self.image_viewer.show()

    def menuOperation(self, action):
        if action == self.actionNew:
            print("new")
        elif action == self.actionOpen:
            self.getImage()
        elif action == self.actionClose:
            app.exit()

    def pasteImage(self):
        """
        由快捷键"Ctrl+V"触发
        修改工作图片的image和pixmap文件
        将imageLabel的显示的图片修改为剪切板图片
        修改图片信息栏imageTextEdit的显示信息
        清空图片路径pathLabel，修改图片名nameEdit信息
        """
        try:
            self.flower_pixmap = ImageGrab.grabclipboard().toqpixmap()
        except AttributeError as e:
            print(e)
            print("当前剪切板项非图片")
            return
        # self.flower_image = self.flower_pixmap.toImage()  # QPixmap -> QImage
        self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
        self.imageLabel.setPixmap(self.flower_pixmap)
        self.imageTextEdit.setText(
            "<p>图片分辨率：<b><font color=red>{}×{}</font></b></p>"
            "<p>图片格式：<b><font color=red>{}</font></b></p>"
            "<p>色彩模式：<b><font color=red>{}</font></b></p>".format(
                self.flower_image.size[0], self.flower_image.size[1], self.flower_image.format,
                self.flower_image.mode))
        self.pathLabel.setText("")
        self.nameEdit.setText("剪切板临时文件")

    def getImage(self):
        """
        槽函数
        获取图片
        """
        # AI线程启动参数预加载
        print("AI Thread is running: preClassify")
        self.AIThread.setOperation("preClassify")
        self.AIThread.start()
        try:
            # 获取文件地址
            file, _ = QFileDialog.getOpenFileName(self, "Open file",
                                                  "D:\\AI_LEARNING_PDF\\deep learning\\flower_images",
                                                  "Image Files (*.jpg *.png)")
            if file:
                self.flower_path = file  # 获取文件地址
                directory_path, self.flower_name = os.path.split(file)  # 获取花朵文件名
                self.flower_pixmap = QPixmap(file)  # 获取花朵图片
                self.pathLabel.setText(directory_path)  # 显示文件夹地址
                self.nameEdit.setText(self.flower_name)  # 显示文件名
                self.imageLabel.setPixmap(self.flower_pixmap)  # 显示花朵图片
                self.resultLabel.setText("{}的预测结果：".format(self.flower_name))  # 预加载处理结果
                self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
                self.imageTextEdit.setText(  # 显示图片信息
                    "<p>图片分辨率：<b><font color=red>{}×{}</font></b></p>"
                    "<p>图片格式：<b><font color=red>{}</font></b></p>"
                    "<p>色彩模式：<b><font color=red>{}</font></b></p>".format(
                        self.flower_image.size[0], self.flower_image.size[1], self.flower_image.format,
                        self.flower_image.mode))
        except FileNotFoundError:
            QMessageBox.warning(self, "警告", "请选择一个有效路径", QMessageBox.Ok)

    def resetImage(self):
        """
        槽函数
        重新导入工作区的图片
        (不包括剪贴板临时图片)
        """
        if self.flower_path == "":  # 未导入图片则不进入函数
            return
        answer = QMessageBox.information(self, "注意", "是否重置原图",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            self.flower_pixmap = QPixmap(self.flower_path)  # 重置QPixmap格式的flower
            self.imageLabel.setPixmap(self.flower_pixmap)  # 重绘image label
            self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)  # 更新Image格式的flower
            self.imageTextEdit.setText(
                "<p>图片分辨率：<b><font color=red>{}×{}</font></b></p>"
                "<p>图片格式：<b><font color=red>{}</font></b></p>"
                "<p>色彩模式：<b><font color=red>{}</font></b></p>".format(
                    self.flower_image.size[0], self.flower_image.size[1], self.flower_image.format,
                    self.flower_image.mode))


    def classifyImage(self):
        """
        槽函数
        进行图片预测
        调用饼图绘制并加载详细信息
        """
        portion, res, index = model_predict(model=self.ai_model, pixmap=self.flower_pixmap)
        prompt = "{}的预测结果：<b><font color=red>{}</font></b>".format(self.flower_name, res)
        self.resultLabel.setText(prompt)
        self.resultLabel_2.setPixmap(QPixmap(u"images/flowers/{}.png".format(res)))
        self._drawPieChart_setDetail(portion, index)

    def _showStatistics(self):
        """
        展示模型统计信息
        """
        model_name = self.ai_model.__class__.__name__
        history_show(model_name)

    def _drawPieChart_setDetail(self, portion, index):
        """
        portion: 各个种类概率
        index: 最大概率索引值
        根据此次统计结果作扇形图并添加detailToolButton按钮
        """
        colors = [(255, 148, 217), (241, 203, 6), (96, 67, 1), (187, 187, 187),
                  (227, 58, 91), (169, 177, 232), (153, 69, 253), (176, 197, 122),
                  (106, 135, 89), (28, 77, 183), (224, 189, 213), (189, 115, 121),
                  (195, 195, 136), (120, 0, 20), (205, 134, 18), (240, 96, 140)]
        series = QPieSeries()
        for i in range(0, len(self.flowers)):
            slice = series.append(self.flowers[i], portion[i])  # 遍历每个扇区
            slice.setColor(QColor(colors[i][0], colors[i][1], colors[i][2]))  # 设置扇区颜色
            slice.setBorderColor(QColor(colors[i][0], colors[i][1], colors[i][2]))  # 设置扇区边缘颜色
            slice.setLabelColor(QColor(colors[i][0], colors[i][1], colors[i][2]))  # 设置扇区标签颜色
            slice.setLabelArmLengthFactor(0.2)  # 设置扇区臂长占比
            if i == index:  # 特殊处理最大扇区
                slice.setExploded(True)  # 突出显示，设置颜色
                slice.setLabelVisible(True)  #
                slice.setPen(QPen(Qt.darkBlue, 2))
            else:  # 处理其他扇区
                if portion[i] > 0.03:  # 所在扇区概率大于0.03则可显示标签
                    slice.setLabelVisible(True)
        # 设置扇形图组件内占比
        series.setPieSize(0.7)
        # 创建QChart实例，它是PyQt5中的类
        chart = QChart()
        # QLegend类是显示图表的图例，先隐藏掉
        # chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        # 设置动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 设置标题
        chart.setTitle("{}模型预测结果".format(self.ai_model.__class__.__name__))
        chart.legend().setVisible(False)
        # 对齐方式
        # chart.legend().setAlignment(Qt.AlignBottom)
        try:
            self.verticalLayout_2.removeWidget(self.pieWidget)
            self.verticalLayout_3.removeWidget(self.detailToolButton)
        except Exception as e:
            print(e)
        # 创建ChartView，它是显示图表的控件
        self.pieWidget = QChartView(chart)
        self.pieWidget.setRenderHint(QPainter.Antialiasing)
        self.pieWidget.isVisible()
        self.verticalLayout_2.addWidget(self.pieWidget)
        self.verticalLayout_3.addWidget(self.detailToolButton)
        QToolTip.setFont(QFont("oldEnglish", 10))
        toolTip = "<p style='white-space:pre'>"  # 富文本标签
        for i in range(0, len(self.flowers)):
            img_path = u"images/flowers/{}.png".format(self.flower_words[i])
            if i == index:
                toolTip += '<img src={} height="24" width="24"><b><font color={}>{}:{:.4%}</font></b>\n'.format(
                    img_path, self.__rgb2html(colors[i]), self.flowers[i], portion[i])
            else:
                toolTip += '<img src={} height="24" width="24"><font color={}>{}:{:.4%}</font>\n'.format(
                    img_path, self.__rgb2html(colors[i]), self.flowers[i], portion[i])
        toolTip += "</p>"  # 富文本结束标签
        self.detailToolButton.setToolTip(toolTip)

    def __rgb2html(self, color):
        # RGB颜色转HTML颜色
        number = '#'
        for i in color:
            shu = hex(int(i))[2:]
            if len(shu) < 2:
                shu = '0' + shu
            number += shu
        return number


class AIModelOperationThread(QThread):
    """
    AI操作线程
    """
    load_signal = Signal(Model)
    load_failed_signal = Signal()
    preload_signal = Signal(Model)
    classify_res_signal = Signal(int, str)

    def __init__(self, parent=None):
        super(AIModelOperationThread, self).__init__(parent)
        print("AIThread Initial")
        self.operation = "load"
        self.files = []
        self.ai_model = EfficientNetB7()

    def run(self) -> None:
        if self.operation == "load":
            # AI线程进行模型初始化操作
            load_success = load_model(self.ai_model)
            if not load_success:
                self.load_failed_signal.emit()
            else:
                self.load_signal.emit(self.ai_model)
            print("AI Thread has finished loading")
        elif self.operation == "preClassify":
            # AI线程参数预加载操作
            model_predict(self.ai_model, QPixmap("./images/帮助.png"))
            self.preload_signal.emit(self.ai_model)
            print("AI Thread has finished preClassifying")

        elif self.operation == "classify":
            for i, file in enumerate(self.files):
                _, res, _ = model_predict(self.ai_model, QPixmap(file))
                self.classify_res_signal.emit(i, res)
            print("AI Thread has finished classifying")

    def setOperation(self, operation: str):
        self.operation = operation

    def setModel(self, model: Model):
        self.ai_model = model

    def setFiles(self, files):
        self.files = files

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec())
