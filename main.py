import os.path
import shutil
import sys

from PIL import ImageGrab
from PySide6.QtCore import QEvent, QPoint, QRect, QThread, Signal
from PySide6.QtGui import QAction, Qt, QIcon, QColor, QCursor, QKeySequence, QShortcut, QBitmap
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QMenu, \
    QProgressBar, QApplication, QGraphicsDropShadowEffect

from AIModel.cnn_models import *
from AIModel.data_process import *
from help_window import HelpWindow
from barStack_chart import BarWidget
from image_cutter import ImageCutter
from image_viewer import ImageViewer
from pieSeries_chart import PieWidget
from ui_MainWindowFlower import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    flowers = ["杜鹃花", "叶子花", "山茶花", "康乃馨", "菊  花", "雏  菊",
               "蒲公英", "桂  花", "栀子花", "木槿花", "绣球花", "鸢尾花",
               "丁香花", "百合花", "荷  花", "牵牛花", "水仙花", "桃  花",
               "牡丹花", "蝴蝶兰", "玫瑰花", "樱  花", "向日葵", "郁金香"]

    flower_words = ["azalea", "bougainvillea", "camellia", "carnation", "chrysanthemum", "daisy",
                    "dandelion", "fragrans", "gardenia", "hibiscus", "hydrangea", "iris",
                    "lilac", "lily", "lotus", "morningglory", "narcissus", "peachflower",
                    "peony", "phalaenopsis", "rose", "sakura", "sunflower", "tulip"]

    colors = [
        (222, 60, 60), (255, 148, 217), (245, 156, 185), (218, 187, 171), (236, 181, 1), (241, 203, 6),
        (96, 67, 1), (229, 223, 105), (187, 187, 187), (227, 58, 91), (169, 177, 232), (153, 69, 253),
        (216, 158, 221), (176, 197, 122), (106, 135, 89), (28, 77, 183), (249, 245, 138), (224, 189, 213),
        (210, 111, 173), (185, 73, 79), (120, 0, 20), (181, 97, 127), (205, 134, 18), (240, 96, 140)
    ]

    def __init__(self):
        super(MyMainWindow, self).__init__()
        # AI线程初始化
        self.initAIThread()
        # 主窗口蒙版初始化
        self.initMainWindowMask()
        # 全局变量初始化
        self.flower_path = ""
        self.flower_image = None
        self.batchDirectory = ""  # 记录批量图片保存路径
        self.files = []  # 记录已选中的批量图片路径
        self.setupUi(self)  # GUI界面初始化(Viewer)
        self.initUI()  # 额外GUI初始化
        self.initConnectSlot()  # 业务操作初始化(Controller)连接槽函数
        self.initStyleSheet()  # 初始化样式表

    def initMainWindowMask(self):
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.pix = QBitmap("images/mask.png")
        self.setMask(self.pix)

    def initAIThread(self):
        self.AIThread = AIModelOperationThread()
        self.AIThread.load_signal[Model].connect(self.__loadModel)  # 加载模型
        self.AIThread.load_failed_signal[None].connect(self.__loadFailed)
        self.AIThread.preload_signal[Model].connect(self.__preLoadModel)
        self.AIThread.classify_res_signal[list, str, bool].connect(self.__setClassifyRes)
        self.AIThread.batch_classify_res_signal[int, str].connect(self.__setBatchClassifyRes)
        self.AIThread.batch_classify_finish_signal[None].connect(self.__batchClassifyFinished)
        self.AIThread.deep_classify_finish[None].connect(self.__deepClassifyFinished)
        self.AIThread.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPosition() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_drag:
            # 当左键移动窗体修改偏移值
            self.move(event.globalPosition().toPoint() - self.m_DragPosition.toPoint())
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventFilter(self, watched, event) -> bool:
        """过滤器实现label点击事件"""
        if watched == self.imageLabel:
            if event.type() == QEvent.MouseButtonDblClick:
                self._getImage()
        if watched == self.pathLabel:
            if event.type() == QEvent.MouseButtonDblClick:
                url = self.pathLabel.text()
                if url == "":
                    return QMainWindow.eventFilter(self, watched, event)
                os.startfile(url)
        # 对于其余情况返回默认处理方法
        return QMainWindow.eventFilter(self, watched, event)

    def initUI(self):
        # 菜单栏QAction充当占位符
        self.holderAction = QAction(self)
        space = "  " * 87
        self.holderAction.setText(space)
        self.holderAction.setEnabled(False)
        self.menubar.addAction(self.holderAction)
        # 菜单栏，最小化QAction
        self.lowerAction = QAction(self)
        self.lowerAction.setText("-")
        self.lowerAction.setIcon(QIcon(u"./images/最小化.png"))
        self.lowerAction.triggered.connect(self.lower)
        self.menubar.addAction(self.lowerAction)
        # 菜单栏，退出QAction
        self.closeAction = QAction(self)
        self.closeAction.setText("×")
        self.closeAction.setIcon(QIcon(u"./images/关闭.png"))
        self.closeAction.triggered.connect(self.close)
        self.menubar.addAction(self.closeAction)
        # 定义tableWidget的右键菜单栏
        self.twPopMenu = QMenu()  # tableWidget右键菜单
        self.delAction = QAction(QIcon("./images/删除.png"), "删除")  # tableWidget删除行为
        self.twPopMenu.addAction(self.delAction)  # 行为添加至菜单
        self.delAction.triggered.connect(self.__deleteRow)  # 绑定"删除行为"的槽
        # label预加载
        self.batchImportLabel.setText("已加载图片张数：0张")
        self.statusBar().showMessage("正在加载模型中...")
        self.resultLabel.setText("未导入图片")
        # 初始化堆叠柱状图和扇形图
        self.barChartWidget = BarWidget()
        self.barChartWidget.setStyleSheet(self.styleSheet())
        self.initPieChart()
        # 组件阴影
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(3, 3)  # 偏移
        effect_shadow.setBlurRadius(20)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.imageTextEdit.setGraphicsEffect(effect_shadow)
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(3, 3)  # 偏移
        effect_shadow.setBlurRadius(20)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.statisticsTextEdit.setGraphicsEffect(effect_shadow)
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(3, 3)  # 偏移
        effect_shadow.setBlurRadius(20)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.savePathTextEdit.setGraphicsEffect(effect_shadow)
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(3, 3)  # 偏移
        effect_shadow.setBlurRadius(5)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.convertModeCheckBox.setGraphicsEffect(effect_shadow)
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(3, 3)  # 偏移
        effect_shadow.setBlurRadius(5)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.batchRenameCheckBox.setGraphicsEffect(effect_shadow)

    def initConnectSlot(self):
        # 绑定按钮点击信号
        self.chooseButton.clicked.connect(self._getImage)
        self.batchChooseButton.clicked.connect(self._getBatchImage)
        self.predictButton.clicked.connect(self.__classifyImage)
        self.clearTableButton.clicked.connect(self.__clearTableContent)
        self.clearButton.clicked.connect(self.clearImportContent)
        self.batchPredictButton.clicked.connect(self.__classifyBatchImages)
        self.getDirectoryButton.clicked.connect(self.getBatchDirectory)
        self.getDirectoryButton_2.clicked.connect(self.getDirectory)
        self.batchExportButton.clicked.connect(self._exportBatchImages)
        self.cutButton.clicked.connect(self.__cutImage)
        self.resetButton.clicked.connect(self.__resetImage)
        self.saveButton.clicked.connect(self._saveImage)
        self.statisticsButton.clicked.connect(self.__showBarChartView)
        # 事件过滤器
        self.imageLabel.installEventFilter(self)
        self.imageLabel.pixmap_signal[bool, str, QPixmap].connect(self.__dropImage)
        self.pathLabel.installEventFilter(self)
        # 绑定工具栏触发信号
        self.menu_M.triggered[QAction].connect(self.chooseModel)
        # 绑定菜单栏触发信号
        self.menu.triggered[QAction].connect(self.__menuOperation)
        self.menu_2.triggered[QAction].connect(self.__menuOperation2)
        self.toolBar.actionTriggered[QAction].connect(self.__toolBarOperation)
        # 绑定表格组件点击信号
        self.tableWidget.cellDoubleClicked.connect(self.__viewImage)
        # 绑定表格组件右键菜单信号
        self.tableWidget.customContextMenuRequested.connect(self.__popMenu)
        # 应用程序全局热键
        QShortcut(QKeySequence(self.tr("Ctrl+V")), self, self._pasteImage)

    def initStyleSheet(self):
        style = readQssFile(u"./stylesheet/Ubuntu.qss")
        self.setStyleSheet(style)

    def initPieChart(self):
        self.pieChartWidget = PieWidget(self.groupBox_5, portion=[0] * len(self.flowers))
        self.pieChartWidget.setGeometry(QRect(22, 105, 471, 431))
        self.pieChartWidget.setVisible(True)

    def __preLoadModel(self, model):
        # AI模型预加载
        self.ai_model = model

    def __loadModel(self, model: Model):
        # AI模型初始化(Model)
        self.ai_model = model
        action_name = model.__class__.__name__
        action_name = action_name[0].lower() + action_name[1:] + "Action"
        eval(f"self.{action_name}.setChecked(True)")  # 菜单栏勾选选中模型
        # 恢复部分按钮
        self.menu_M.setEnabled(True)
        self.actionClassify.setEnabled(True)
        self.predictButton.setEnabled(True)
        self.batchPredictButton.setEnabled(True)
        model_name = self.ai_model.__class__.__name__
        QMessageBox.information(self, "成功",
                                "成功导入模型" + model_name,
                                QMessageBox.Ok)
        self.statusBar().showMessage("模型：" + model_name)
        self.predictButton.setToolTip(f"使用{model_name}模型进行预测")

    def __loadFailed(self):
        QMessageBox.warning(self, "错误", "未导入该模型！", QMessageBox.Ok)
        self.menu_M.setEnabled(True)
        self.actionClassify.setEnabled(True)
        self.predictButton.setEnabled(True)
        self.batchPredictButton.setEnabled(True)

    def __setBatchClassifyRes(self, i, res):
        # 收到AI线程批量预测中的每次信号
        icon_path = "images/flowers/{}.png".format(res)
        # 完善tablewidget第三列结果和图标
        self.tableWidget.setItem(i, 2, QTableWidgetItem(QIcon(icon_path), self.flowers[self.flower_words.index(res)]))
        # 添加柱状堆叠图的数据——文件夹: 预测结果
        self.barChartWidget.addData(self.tableWidget.item(i, 0).text(), res)
        self.barChartWidget.initChart()
        text = ""
        for directory, content in self.barChartWidget.data.items():  # 将预测结果按格式输出
            text += "<br /><b><font color=red>{}</font></b>统计如下:<br />&nbsp;&nbsp;&nbsp;&nbsp;".format(directory)
            for flower_word, count in content.items():
                text += "{}共计<b>{}</b>张<br />&nbsp;&nbsp;&nbsp;&nbsp;".format(
                    self.flowers[self.flower_words.index(flower_word)],
                    count)
        self.statisticsTextEdit.setText(text)
        self.progressBar2.setValue(i + 1)

    def __batchClassifyFinished(self):
        # 恢复部分按钮
        self.menu_M.setEnabled(True)
        self.actionClassify.setEnabled(True)
        self.predictButton.setEnabled(True)
        self.batchPredictButton.setEnabled(True)
        self.batchExportButton.setEnabled(True)
        self.batchChooseButton.setEnabled(True)
        self.clearTableButton.setEnabled(True)
        # 删除进度条2
        self.progressBar2.deleteLater()

    def chooseModel(self, model_action):
        if model_action == self.actionCNN:
            model_name = self.ai_model.__class__.__name__
            history_show(model_name)
            return
        if model_action == self.denseNet121Action:
            self.AIThread.setModel(DenseNet121())
        else:
            self.denseNet121Action.setChecked(False)
        if model_action == self.efficientNetB0Action:
            self.AIThread.setModel(EfficientNetB0())
        else:
            self.efficientNetB0Action.setChecked(False)
        if model_action == self.efficientNetB2Action:
            self.AIThread.setModel(EfficientNetB2())
        else:
            self.efficientNetB2Action.setChecked(False)
        if model_action == self.efficientNetB4Action:
            self.AIThread.setModel(EfficientNetB4())
        else:
            self.efficientNetB4Action.setChecked(False)
        if model_action == self.efficientNetB7Action:
            self.AIThread.setModel(EfficientNetB7())
        else:
            self.efficientNetB7Action.setChecked(False)
        if model_action == self.inceptionV3Action:
            self.AIThread.setModel(InceptionV3())
        else:
            self.inceptionV3Action.setChecked(False)
        if model_action == self.vGG19Action:
            self.AIThread.setModel(VGG19())
        else:
            self.vGG19Action.setChecked(False)
        if model_action == self.mobileNetV2Action:
            self.AIThread.setModel(MobileNetV2())
        else:
            self.mobileNetV2Action.setChecked(False)
        # AI线程启动模型加载
        print("AI Thread is running: load")
        self.AIThread.setOperation("load")
        self.AIThread.start()
        self.statusBar().showMessage("模型正在加载中.. ..")
        # 禁用部分按钮
        self.menu_M.setEnabled(False)
        self.actionClassify.setEnabled(False)
        self.predictButton.setEnabled(False)
        self.batchPredictButton.setEnabled(False)

    def getBatchDirectory(self):
        # 选取文件夹
        self.batchDirectory = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                               "./images/image_test")
        self.savePathLineEdit.setText(self.batchDirectory)

    def getDirectory(self):
        # 选取文件夹
        self.directory = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                          "./images/image_test")
        self.savePathTextEdit.setText(self.directory)

    def clearImportContent(self):
        self.resultLabel_2.setPixmap(QPixmap())  # 清空预测结果图标
        self.resultLabel_3.setText("")
        self.flower_path = ""  # 清空图片路径
        self.flower_name = ""  # 清空图片名
        self.flower_image = None
        self.flower_pixmap = None
        self.resultLabel.setText("未导入图片")
        self.resultLabel_2.setPixmap(QPixmap())
        self.pathLabel.setText("")  # 显示文件夹地址
        self.pathLabel.setToolTip("")
        self.nameEdit.setText("")  # 显示文件名
        self.imageLabel.setPixmap(QPixmap(u"./images/打开图片.png"))  # 显示花朵图片
        self.imageTextEdit.setText("")
        self.initPieChart()

    def _getBatchImage(self):
        # AI线程启动参数预加载
        print("AI Thread is running: preClassify")
        self.AIThread.setOperation("preClassify")
        self.AIThread.start()
        try:
            # 获取选择图片
            files, _ = QFileDialog.getOpenFileNames(self, "Open files",
                                                    "./images/image_test",
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
            print(e)
            QMessageBox.warning(self, "警告", "请选择一个有效路径", QMessageBox.Ok)

    def __classifyBatchImages(self):
        # 每次进行预测时清空之前的预测结果
        self.barChartWidget.clearData()
        # AI线程启动批量预测
        print("AI Thread is running: classify")
        self.AIThread.setFiles(self.files)
        self.AIThread.setOperation("batchClassify")
        self.AIThread.start()
        self.statisticsTextEdit.setText("")
        # 禁用部分按钮
        self.menu_M.setEnabled(False)
        self.actionClassify.setEnabled(False)
        self.predictButton.setEnabled(False)
        self.batchPredictButton.setEnabled(False)
        self.batchExportButton.setEnabled(False)
        self.batchChooseButton.setEnabled(False)
        self.clearTableButton.setEnabled(False)

        # 批量预测-进度条
        self.progressBar2 = QProgressBar(self.groupBox_2)
        self.progressBar2.setGeometry(130, 30, 281, 23)
        self.progressBar2.setMaximum(len(self.files))
        self.progressBar2.setValue(0)
        self.progressBar2.setVisible(True)

    def __clearTableContent(self):
        res = QMessageBox.information(self, "确认", "是否清除已导入图片",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.tableWidget.setRowCount(0)
            self.tableWidget.clearContents()
            self.files.clear()
            self.batchImportLabel.setText("已加载图片张数：{}".format(len(self.files)))
            self.statisticsTextEdit.setText("")

    def __popMenu(self, point: QPoint):
        try:
            item = self.tableWidget.itemAt(point)
            self.delete_row_num = item.row()
            # 绑定删除事件的信号
            self.twPopMenu.exec(QCursor().pos())
        except Exception as e:
            print(e)
            self.delete_row_num = -1  # 置为无效值

    def __deleteRow(self):
        try:
            row_num = self.delete_row_num
            self.tableWidget.removeRow(row_num)
            self.files.pop(row_num)
            self.batchImportLabel.setText("已加载图片张数：{}".format(len(self.files)))
        except Exception as e:
            print(e)

    def _exportBatchImages(self):
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
            if self.batchRenameCheckBox.isChecked():
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
            if self.convertModeCheckBox.isChecked():
                img = Image.open(des_path)
                img = img.convert("RGB")
                os.remove(des_path)
                des_path = des_path.split(".")[0] + ".jpg"
                while os.path.isfile(des_path):
                    # 判断是否有重名文件，避免覆盖
                    prefix, postfix = save_path.split(".")
                    des_path = "{} ({}).{}".format(prefix, i, postfix)
                    i += 1
                img.save(des_path)
        if not exported_flag:
            # 此次未经过导出
            QMessageBox.information(self, "注意", "请先进行图片预测", QMessageBox.Ok)
        else:
            os.startfile(path)

    def _saveImage(self):
        if self.flower_pixmap is None:
            return
        image_name = self.flower_name
        if self.saveNameEdit.text() is not None:
            image_name = self.saveNameEdit.text()
        try:
            save_path = self.directory
        except AttributeError:
            QMessageBox.information(self, "错误", "请先选择保存路径")
            return
        if not os.path.exists(save_path):
            QMessageBox.information(self, "错误", "请选择正确的文件夹地址")
            return
        save_path = save_path + "/" + image_name  # 拼接保存路径：文件夹+文件原始名称
        try:
            self.flower_image.save(save_path)
        except ValueError:
            QMessageBox.information(self, "错误", "请输入正确的文件扩展名(*.png *.jpg *.gif *.bmp ...)")
            return
        answer = QMessageBox.information(self, "保存成功",
                                         "文件路径为：{}".format(save_path), QMessageBox.Open | QMessageBox.Ok)
        if answer == QMessageBox.Open:
            os.startfile(save_path)

    def __dropImage(self, tag: bool, url: str, pixmap: QPixmap):
        """
        tag: 标识是否为浏览器文件
        url: 图片的url(本地地址和浏览器链接)
        """
        if pixmap.isNull():
            print("请输入正确的图片url！")
            return
        self.flower_path = url  # 获取图片的url
        self.flower_pixmap = pixmap  # 获取花朵图片
        self.flower_image = ImageQt.fromqpixmap(pixmap)
        if tag:
            self.flower_name = "浏览器临时文件"  # 获取花朵文件名
            url_path = url
        else:
            url_path, self.flower_name = os.path.split(url)
        self.directory_path = url_path
        self.update()

    def __cutImage(self):
        if self.flower_pixmap is None:
            return
        self.image_cutter = ImageCutter(image=self.flower_pixmap)
        self.image_cutter.setStyleSheet(self.styleSheet())
        self.image_cutter.save_signal.connect(self.__passImage)
        self.image_cutter.show()

    def __passImage(self, pixmap):
        self.flower_pixmap = pixmap
        self.flower_image = ImageQt.fromqpixmap(pixmap)
        self.update()

    def __viewImage(self, row):
        self.image_viewer = ImageViewer(image=self.files[row], background=QColor(235, 255, 244))
        self.image_viewer.setStyleSheet(self.styleSheet())
        self.image_viewer.show()

    def __menuOperation(self, action):
        if action == self.actionClose:
            app.exit()

    def __menuOperation2(self, action):
        if action == self.actionAbout:
            self.helpWindow = HelpWindow()
            self.helpWindow.setStyleSheet(self.styleSheet())
            self.helpWindow.show()
        if action == self.actionMyStyle:
            self.setStyleSheet(readQssFile(u"./stylesheet/style.qss"))
        if action == self.actionUbuntuStyle:
            self.setStyleSheet(readQssFile(u"./stylesheet/Ubuntu.qss"))
        if action == self.actionAMOLED:
            self.setStyleSheet(readQssFile(u"./stylesheet/AMOLED.qss"))
        if action == self.actionAqua:
            self.setStyleSheet(readQssFile(u"./stylesheet/Aqua.qss"))
        if action == self.actionConsoleStyle:
            self.setStyleSheet(readQssFile(u"./stylesheet/ConsoleStyle.qss"))
        if action == self.actionElegantDark:
            self.setStyleSheet(readQssFile(u"./stylesheet/ElegantDark.qss"))
        if action == self.actionMacOS:
            self.setStyleSheet(readQssFile(u"./stylesheet/MacOS.qss"))
        if action == self.actionManjaroMix:
            self.setStyleSheet(readQssFile(u"./stylesheet/ManjaroMix.qss"))
        if action == self.actionMaterialDark:
            self.setStyleSheet(readQssFile(u"./stylesheet/MaterialDark.qss"))

    def __toolBarOperation(self, action):
        if action == self.actionClassify:
            answer = QMessageBox.question(self, "是否开启深度识别", "这可能需要花费较长时间",
                                          QMessageBox.Yes | QMessageBox.No)
            if answer == QMessageBox.Yes:
                # 绑定actionClassify
                self.__deepClassify()
        if action == self.actionOpen:
            tab = self.tabWidget.currentWidget()
            if tab == self.tab1:
                self._getImage()
            elif tab == self.tab2:
                self._getBatchImage()
        if action == self.actionSave:
            tab = self.tabWidget.currentWidget()
            if tab == self.tab1:
                self._saveImage()
            elif tab == self.tab2:
                self._exportBatchImages()

    def __deepClassify(self):
        # 深度预测--进度条
        self.progressBar1 = QProgressBar(self.layoutWidget)
        self.progressBar1.setMaximum(147)
        self.horizontalLayout_3.addWidget(self.progressBar1)
        self.progressBar1.setValue(2)
        # 进行深度预测
        print("AI Thread is running: deepClassify")
        self.AIThread.setFiles(self.flower_pixmap)
        self.AIThread.setOperation("deepClassify")
        self.AIThread.start()
        # 禁用部分按钮
        self.menu_M.setEnabled(False)
        self.actionClassify.setEnabled(False)
        self.predictButton.setEnabled(False)
        self.batchPredictButton.setEnabled(False)

    def __deepClassifyFinished(self):
        self.progressBar1.setValue(147)
        self.horizontalLayout_3.removeWidget(self.progressBar1)
        self.progressBar1.deleteLater()
        QMessageBox.information(self, "成功", "完成图像的深度预测！", QMessageBox.Ok)
        # 恢复按钮
        self.menu_M.setEnabled(True)
        self.actionClassify.setEnabled(True)
        self.predictButton.setEnabled(True)
        self.batchPredictButton.setEnabled(True)

    def _pasteImage(self):
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
        self.directory_path = ""
        self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
        self.flower_name = "剪贴板临时文件"
        self.update()

    def _getImage(self):
        """
        槽函数
        获取图片
        """
        try:
            # 获取文件地址
            file, _ = QFileDialog.getOpenFileName(self, "Open file",
                                                  "./images/image_test",
                                                  "Image Files (*.jpg *.png)")
            if file:
                self.flower_path = file  # 获取文件地址
                self.directory_path, self.flower_name = os.path.split(file)  # 获取花朵文件名
                self.flower_pixmap = QPixmap(file)  # 获取花朵图片
                self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
                self.update()
        except FileNotFoundError:
            QMessageBox.warning(self, "警告", "请选择一个有效路径", QMessageBox.Ok)

    def __resetImage(self):
        """
        槽函数
        重新导入工作区的图片
        (不包括剪贴板临时图片)
        """
        # answer = QMessageBox.information(self, "注意", "是否重置原图",
        #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # if answer == QMessageBox.Yes:
        try:
            if os.path.exists(self.flower_path):  # 如果是本地url，则直接重新读取重置
                self.flower_pixmap = QPixmap(self.flower_path)
            else:  # 如果不是本地url，则重置为drop时的pixmap
                self.flower_pixmap = QPixmap(self.imageLabel.my_pixmap)  # 重置QPixmap格式的flower
            self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)  # 更新Image格式的flower
            self.update()
        except TypeError as e:
            print("__resetImage")
            print(e)

    def __classifyImage(self):
        """
        槽函数
        进行图片预测
        调用饼图绘制并加载详细信息
        """
        if self.flower_pixmap is None:
            return
        print("AI Thread is running: classify")
        self.AIThread.setFiles(self.flower_pixmap)
        self.AIThread.setOperation("classify")
        self.AIThread.start()
        # 禁用部分按钮
        self.menu_M.setEnabled(False)
        self.actionClassify.setEnabled(False)
        self.predictButton.setEnabled(False)
        self.batchPredictButton.setEnabled(False)

    def __setClassifyRes(self, portion, res, tag=False):
        def getMaxPortion(array, iteration):
            # 获取前iteration个的(结果，占比，颜色)
            top_res = []
            top_per = []
            top_color = []
            for _ in range(0, iteration):
                max_idx = array.index(max(array))
                top_res.append(self.flowers[max_idx])
                top_per.append(max(array))
                top_color.append(rgb2html(self.colors[max_idx]))
                array[max_idx] = 0
            return top_res, top_per, top_color

        idx = self.flower_words.index(res)
        name = self.flowers[idx]
        prompt1 = '{}的预测结果：<b><font size = "5" color={}>{}</font></b>'.format(self.flower_name,
                                                                              rgb2html(self.colors[idx]), name)
        self.resultLabel.setText(prompt1)
        self.resultLabel_2.setPixmap(QPixmap("images/flowers/{}.png".format(res)))
        num = 3  # 显示概率最大的个数
        res, per, color = getMaxPortion(portion.copy(), num)
        prompt2 = "预测结果：<b>"
        for i in range(0, num):
            prompt2 += "<font color={}>{}:{:.4%}&nbsp;&nbsp;</font>".format(color[i], res[i], per[i])
        prompt2 += "</b>"
        self.resultLabel_3.setText(prompt2)
        self.resultLabel_3.setToolTip("{}: {:.4%}".format(res[0], per[0]))
        # tag: 标记是否为最大加权网络
        model_name = "综合加权网络" if tag is True else self.ai_model.__class__.__name__
        self.pieChartWidget.setPortion(portion)
        self.pieChartWidget.initChart(model_name=model_name)
        if tag:
            self.progressBar1.setValue(self.progressBar1.value() + 21)
        # 禁用部分按钮
        if not tag:  # 非深度预测时一次预测时结束进行按钮释放
            self.menu_M.setEnabled(True)
            self.actionClassify.setEnabled(True)
            self.predictButton.setEnabled(True)
            self.batchPredictButton.setEnabled(True)

    def __showBarChartView(self):
        self.barChartWidget.show()

    def update(self) -> None:
        print("update")
        self.pathLabel.setText(self.directory_path)  # 更新显示文件夹地址
        self.pathLabel.setToolTip("双击打开")  # 更新显示文件夹地址提示
        self.nameEdit.setText(self.flower_name)  # 更新显示文件名
        self.imageLabel.setPixmap(self.flower_pixmap)  # 更新显示花朵图片
        self.resultLabel.setText("{}的预测结果：".format(self.flower_name))  # 更新预加载处理结果
        mode = "<p>色彩模式：<b>"
        for c in self.flower_image.mode:
            if c == 'R':
                mode += "<font color=red>R</font>"
            elif c == 'G':
                mode += "<font color=green>G</font>"
            elif c == 'B':
                mode += "<font color=blue>B</font>"
            elif c == 'A' or c == "K":
                mode += f"<font color=black>{c}</font>"
            elif c == 'C':
                mode += "<font color=aqua>C</font>"
            elif c == 'M':
                mode += "<font color=#8B008B>M</font>"
            elif c == 'Y':
                mode += "<font color=yellow>Y</font>"
        mode += "</b></p>"
        self.imageTextEdit.setText(  # 更新显示图片信息
            "<p>图片名：<b><font color=black>{}</font></b></p>"
            "<p>图片分辨率：<b><font color=black>{}×{}</font></b></p>"
            "<p>图片格式：<b><font color=black>{}</font></b></p>"
            "{}".format(
                self.flower_name,
                self.flower_image.size[0], self.flower_image.size[1],
                self.flower_image.format,
                mode))
        self.resultLabel_2.setPixmap(QPixmap())  # 更新
        self.resultLabel_3.setText("")
        self.resultLabel_3.setToolTip("")
        self.initPieChart()


class AIModelOperationThread(QThread):
    """
    AI操作线程
    """
    load_signal = Signal(Model)
    load_failed_signal = Signal()
    preload_signal = Signal(Model)
    batch_classify_res_signal = Signal(int, str)
    batch_classify_finish_signal = Signal()
    # 传递结果列表portion, 结果值res, 是否为深度测评tag
    classify_res_signal = Signal(list, str, bool)
    deep_classify_finish = Signal()

    flower_words = MyMainWindow.flower_words

    def __init__(self, parent=None):
        super(AIModelOperationThread, self).__init__(parent)
        print("AIThread Initial")
        self.operation = "load"
        self.ai_model = EfficientNetB0()
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
            self.batch_classify_res_signal[int, str].emit(i, res)
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
        x = get_input_x(QPixmap("./images/帮助.png"))
        model_predict(self.ai_model, x)
        self.preload_signal[Model].emit(self.ai_model)
        print("AI Thread has finished preClassifying")

    def setOperation(self, operation: str):
        self.operation = operation

    def setModel(self, model: Model):
        self.ai_model = model

    def setFiles(self, files):
        self.files = files


def readQssFile(qss_file_name):
    # 读入Qss
    with open(qss_file_name, 'r', encoding='UTF-8') as file:
        return file.read()


def rgb2html(color):
    # RGB颜色转HTML颜色
    number = '#'
    for i in color:
        shu = hex(int(i))[2:]
        if len(shu) < 2:
            shu = '0' + shu
        number += shu
    return number


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec())
