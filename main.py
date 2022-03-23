import os.path
import pathlib
import sys

from PIL import ImageGrab
from PySide6.QtCore import QEvent, QPoint, QRect
from PySide6.QtGui import QAction, Qt, QIcon, QColor, QCursor, QKeySequence, QShortcut, QBitmap, QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMenu, \
    QProgressBar, QApplication, QGraphicsDropShadowEffect, QSystemTrayIcon, QComboBox, QTextEdit, QLineEdit, \
    QCheckBox, QPushButton, QSpinBox

from AIModel.cnn_models import *
from AIModel.data_process import *
from ai_model_thread import AIModelOperationThread
from barStack_chart import BarWidget
from cursor_gif import QCursorGif
from help_window import HelpWindow
from image_cutter import ImageCutter
from image_viewer import ImageViewer
from notification import NotificationWindow
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
        self.flower_pixmap = None
        self.flower_image = None
        self.batchDirectory = ""  # 记录批量图片保存路径
        self.files = []  # 记录已选中的批量图片路径
        self.setupUi(self)  # GUI界面初始化(Viewer)
        self.initUI()  # 额外GUI初始化
        self.initGraphicsShadow()
        self.initConnectSlot()  # 业务操作初始化(Controller)连接槽函数
        self.initStyleSheet()  # 初始化样式表

    def initMainWindowMask(self):
        # 设置主窗口蒙版，形成圆角窗口
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.pix = QBitmap(u"./images/mask.png")
        self.setMask(self.pix)

    def initAIThread(self):
        self.AIThread = AIModelOperationThread(window=self)
        self.AIThread.load_signal.connect(self.__loadModel)  # 加载模型
        self.AIThread.load_failed_signal[None].connect(self.__loadFailed)
        self.AIThread.preload_signal.connect(self.__preLoadModel)
        self.AIThread.classify_res_signal[list, str, bool].connect(self.__setClassifyRes)
        self.AIThread.batch_classify_res_signal[int, str, bool].connect(self.__setBatchClassifyRes)
        self.AIThread.batch_classify_finish_signal[None].connect(self.__batchClassifyFinished)
        self.AIThread.deep_classify_finish[None].connect(self.__deepClassifyFinished)
        self.AIThread.start()

    def __loadModel(self, model):
        # AI模型初始化(Model)
        self.ai_model = model
        action_name = model.__class__.__name__
        action_name = action_name[0].lower() + action_name[1:] + "Action"
        eval(f"self.{action_name}.setChecked(True)")  # 菜单栏勾选选中模型
        # 恢复部分按钮
        self._release_button()
        model_name = self.ai_model.__class__.__name__
        NotificationWindow.success(self, "成功", f"成功导入模型{model_name}", time=3000)
        self.statusBar().showMessage("模型：" + model_name)
        self.predictButton.setToolTip(f"使用{model_name}模型进行预测")

    def __loadFailed(self):
        NotificationWindow.error(self, "错误", "未导入该模型!", time=3000)
        self.statusBar().showMessage("请重新选择已导入模型...")
        self._release_button()

    def __preLoadModel(self, model):
        # AI模型预加载
        self.ai_model = model

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
        model_name = "综合加权网络" if tag is True else self.ai_model.__class__.__name__
        prompt1 = '{}的预测结果：<b><font size = "5" color={}>{}</font></b>'.format(self.flower_name,
                                                                              rgb2html(self.colors[idx]), name)
        self.resultLabel.setText(prompt1)
        self.resultLabel_2.setPixmap(QPixmap(u"images/flowers/{}.png".format(res)))
        num = 3  # 显示概率最大的个数
        res, per, color = getMaxPortion(portion.copy(), num)
        prompt2 = f"<p>{model_name}预测结果：<b>"
        for i in range(0, num):
            prompt2 += "<font color={}>{}：{:.2%}&nbsp;</font>".format(color[i], res[i], per[i])
        prompt2 += "</b></p>"
        text = self.imageTextEdit.toHtml() + prompt2
        self.imageTextEdit.setText(text)
        # tag: 标记是否为最大加权网络

        self.pieChartWidget.setPortion(portion)
        self.pieChartWidget.initChart(model_name=model_name)
        if tag:
            self.progressBar1.setValue(self.progressBar1.value() + 1)
        # 禁用部分按钮
        if not tag:  # 非深度预测时一次预测时结束进行按钮释放
            self._release_button()

    def __setBatchClassifyRes(self, i, res, tag: bool):
        # 收到AI线程批量预测中的每次信号,tag=0表示预测操作,tag=True表示到处操作
        if not tag:
            icon_path = u"images/flowers/{}.png".format(res)
            # 完善tablewidget第三列结果和图标
            self.tableWidget.setItem(i, 2,
                                     QTableWidgetItem(QIcon(icon_path), self.flowers[self.flower_words.index(res)]))
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
        self._release_button()
        # 清空进度条
        self.progressBar2.setValue(0)

    def __deepClassifyFinished(self):
        self.progressBar1.setValue(len(get_installed_model()[0]))
        self.horizontalLayout_3.removeWidget(self.progressBar1)
        self.progressBar1.deleteLater()
        NotificationWindow.success(self, "成功", "完成图像的深度预测！")
        # 恢复按钮
        self._release_button()

    def initUI(self):
        # 设置忙碌光标图片数组
        self.my_cursor = QCursorGif([u'./images/Cursors/%d.png' % i for i in range(8)])
        self.my_cursor.setCursorTimeout(100)
        # 系统托盘图标
        tray_menu = QMenu(self)
        tray_menu.addMenu(self.menu_M)
        tray_menu.addAction(self.actionOpen)
        tray_menu.addAction(self.actionClose)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(u"./images/AI识别.ico"))
        self.tray_icon.show()
        self.tray_icon.setToolTip("花朵图像识别")
        self.tray_icon.activated.connect(self.__tray_activated)
        self.tray_icon.setContextMenu(tray_menu)
        # # 菜单栏QAction充当占位符
        self.holderAction = QMenu(self)
        space = "  " * 84
        self.holderAction.setTitle(space)
        # self.holderAction.setEnabled(False)
        self.holderAction.setDisabled(True)
        self.menubar.addMenu(self.holderAction)
        # 菜单栏，固定窗口最前QAction
        self.pinAction = QAction(self)
        self.pinAction.setText("-")
        self.pinAction.setIcon(QIcon(u"./images/图钉关.png"))
        self.pinAction.triggered.connect(self.__switch_windows_flags)
        self.pinAction.setToolTip("置于窗口最前")
        self.pinAction.setStatusTip("置于窗口最前")
        self.pinAction.setCheckable(True)
        self.window_state = False  # 标记是否置于窗口最前
        # self.toolBar.addAction(self.pinAction)
        self.menubar.addAction(self.pinAction)
        # 菜单栏，最小化QAction
        self.lowerAction = QAction(self)
        self.lowerAction.setText("-")
        self.lowerAction.setIcon(QIcon(u"./images/最小化.png"))
        self.lowerAction.triggered.connect(self.showMinimized)
        self.lowerAction.setStatusTip("窗口最小化")
        self.menubar.addAction(self.lowerAction)
        # 菜单栏，退出QAction
        self.closeAction = QAction(self)
        self.closeAction.setText("×")
        self.closeAction.setIcon(QIcon(u"./images/关闭.png"))
        self.closeAction.triggered.connect(self.close)
        self.closeAction.setStatusTip("退出程序")
        self.menubar.addAction(self.closeAction)
        # 定义tableWidget的右键菜单栏
        self.twPopMenu = QMenu()  # tableWidget右键菜单
        self.delAction = QAction(QIcon(u"./images/删除.png"), "删除")  # tableWidget删除行为
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
        # 未导入模型按钮取消
        _, uninstalled = get_installed_model()
        for model_name in uninstalled:
            action_name = model_name[0].lower() + model_name[1:] + "Action"
            eval(f"self.menu_M.removeAction(self.{action_name})")

    def __tray_activated(self, activation: QSystemTrayIcon.ActivationReason):
        # 系统托盘激活事件
        if activation == QSystemTrayIcon.Trigger:
            # 系统托盘被左键单击：显示软件
            self.showNormal()

    def __switch_windows_flags(self):
        if self.window_state:
            self.window_state = False
            self.pinAction.setChecked(False)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.pinAction.setStatusTip("置于窗口最前")
            self.pinAction.setIcon(QIcon(u"./images/图钉关.png"))
            self.show()
        else:
            self.window_state = True
            self.pinAction.setChecked(True)
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.pinAction.setStatusTip("取消置于窗口最前")
            self.pinAction.setIcon(QIcon(u"./images/图钉开.png"))
            self.show()

    def initGraphicsShadow(self):
        print("initGraphicsShadow")
        # GroupBox组件阴影
        effect_shadow_group_box = QGraphicsDropShadowEffect(self)
        effect_shadow_group_box.setOffset(1, 1)  # 偏移
        effect_shadow_group_box.setBlurRadius(20)  # 阴影半径
        effect_shadow_group_box.setColor(Qt.gray)
        self.groupBox.setGraphicsEffect(effect_shadow_group_box)
        # TextEdit组件阴影
        for child in self.findChildren(QTextEdit):
            effect_shadow_text_edit = QGraphicsDropShadowEffect(self)
            effect_shadow_text_edit.setOffset(3, 3)  # 偏移
            effect_shadow_text_edit.setBlurRadius(20)  # 阴影半径
            effect_shadow_text_edit.setColor(Qt.gray)
            child.setGraphicsEffect(effect_shadow_text_edit)
        # LineEdit组件阴影
        for child in self.findChildren(QLineEdit):
            effect_shadow_line_edit = QGraphicsDropShadowEffect(self)
            effect_shadow_line_edit.setOffset(2, 2)  # 偏移
            effect_shadow_line_edit.setBlurRadius(20)  # 阴影半径
            effect_shadow_line_edit.setColor(Qt.gray)
            child.setGraphicsEffect(effect_shadow_line_edit)
        # CheckBox组件阴影
        for child in self.findChildren(QCheckBox):
            effect_shadow_check_box = QGraphicsDropShadowEffect(self)
            effect_shadow_check_box.setOffset(1, 1)  # 偏移
            effect_shadow_check_box.setBlurRadius(20)  # 阴影半径
            effect_shadow_check_box.setColor(Qt.gray)
            child.setGraphicsEffect(effect_shadow_check_box)
        # PushButton组件阴影
        for child in self.findChildren(QPushButton):
            effect_shadow_push_button = QGraphicsDropShadowEffect(self)
            effect_shadow_push_button.setOffset(1, 1)  # 偏移
            effect_shadow_push_button.setBlurRadius(10)  # 阴影半径
            effect_shadow_push_button.setColor(Qt.gray)
            child.setGraphicsEffect(effect_shadow_push_button)
        # ComboBox组件阴影
        for child in self.findChildren(QComboBox):
            effect_shadow_combo_box = QGraphicsDropShadowEffect(self)
            effect_shadow_combo_box.setOffset(2, 2)
            effect_shadow_combo_box.setBlurRadius(10)
            effect_shadow_combo_box.setColor(Qt.gray)
            child.setGraphicsEffect(effect_shadow_combo_box)
        # SpinBox组件阴影
        for child in self.findChildren(QSpinBox):
            effect_shadow_spin_box = QGraphicsDropShadowEffect(self)
            effect_shadow_spin_box.setOffset(2, 2)
            effect_shadow_spin_box.setBlurRadius(20)
            effect_shadow_spin_box.setColor(Qt.gray)
            child.setGraphicsEffect(effect_shadow_spin_box)

    def initConnectSlot(self):
        # 绑定按钮点击信号
        self.chooseButton.clicked.connect(self._getImage)
        self.batchChooseButton.clicked.connect(self._getBatchImage)
        self.predictButton.clicked.connect(self.__classifyImage)
        self.clearTableButton.clicked.connect(self.__clearTableContent)
        self.clearButton.clicked.connect(self.__clearImportContent)
        self.batchPredictButton.clicked.connect(self.__classifyBatchImages)
        self.getDirectoryButton.clicked.connect(self.getBatchDirectory)
        self.getDirectoryButton_2.clicked.connect(self.getDirectory)
        self.batchExportButton.clicked.connect(self._exportBatchImages)
        self.cutButton.clicked.connect(self.__cutImage)
        self.resetButton.clicked.connect(self.__resetImage)
        self.saveButton.clicked.connect(self._saveImage)
        self.statisticsButton.clicked.connect(self.__showBarChartView)
        self.comboBox.currentTextChanged[str].connect(self.__changeComboBox)
        self.comboBox_2.currentTextChanged[str].connect(self.__changeComboBox)
        self.spinBox_width.valueChanged.connect(self.__change_width_spin_box)
        self.spinBox_height.valueChanged.connect(self.__change_height_spin_box)
        self.spinBox_width_2.valueChanged.connect(self.__change_width_spin_box)
        self.spinBox_height_2.valueChanged.connect(self.__change_height_spin_box)
        # 事件过滤器
        self.imageLabel.installEventFilter(self)
        self.imageLabel.pixmap_signal[bool, str, QPixmap].connect(self.__dropImage)
        self.pathLabel.installEventFilter(self)
        # 绑定工具栏触发信号
        self.menu_M.triggered[QAction].connect(self.__chooseModel)
        # 绑定菜单栏触发信号
        self.menu.triggered[QAction].connect(self.__menuOperation)
        self.menu_2.triggered[QAction].connect(self.__menuOperation2)
        self.menu_style.triggered[QAction].connect(self.__menu_style_operation)
        self.toolBar.actionTriggered[QAction].connect(self.__toolBarOperation)
        # 绑定表格组件点击信号
        self.tableWidget.cellDoubleClicked.connect(self.__viewImage)
        # 绑定表格组件右键菜单信号
        self.tableWidget.customContextMenuRequested.connect(self.__popMenu)
        # 应用程序全局热键
        QShortcut(QKeySequence(self.tr("Ctrl+V")), self, self._pasteImage)

    def __change_width_spin_box(self, value):
        self.spinBox_width.setValue(value)
        self.spinBox_width.setToolTip(f"宽:{value}")
        self.label_res.setToolTip(f"图像分辨率：{self.spinBox_width.value()}×{self.spinBox_height.value()}")
        self.spinBox_width_2.setValue(value)
        self.spinBox_width_2.setToolTip(f"宽:{value}")
        self.label_res.setToolTip(f"图像分辨率：{self.spinBox_width_2.value()}×{self.spinBox_height_2.value()}")

    def __change_height_spin_box(self, value):
        self.spinBox_height.setValue(value)
        self.spinBox_height.setToolTip(f"长:{value}")
        self.label_res.setToolTip(f"图像分辨率：{self.spinBox_width.value()}×{self.spinBox_height.value()}")
        self.spinBox_height_2.setValue(value)
        self.spinBox_height_2.setToolTip(f"长:{value}")
        self.label_res.setToolTip(f"图像分辨率：{self.spinBox_width_2.value()}×{self.spinBox_height_2.value()}")

    def initPieChart(self):
        self.pieChartWidget = PieWidget(self.groupBox_5, portion=[0] * len(self.flowers))
        self.pieChartWidget.setGeometry(QRect(22, 75, 471, 461))
        self.pieChartWidget.setVisible(True)

    def __chooseModel(self, model_action):
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
        self._lock_button()

    def getBatchDirectory(self):
        # 选取文件夹
        self.batchDirectory = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                               u"./images/image_test")
        self.savePathLineEdit.setText(self.batchDirectory)

    def getDirectory(self):
        # 选取文件夹
        self.directory = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                          u"./images/image_test")
        self.savePathTextEdit.setText(self.directory)

    def __clearImportContent(self):
        NotificationWindow.info(self, "是否确认",
                                "<font color=red><b><u>清除当前的图片及相关信息</u></b></font>",
                                callback=self.__clear)

    def __clear(self):
        self.resultLabel_2.setPixmap(QPixmap())  # 清空预测结果图标
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
        # print("AI Thread is running: preClassify")
        # self.AIThread.setOperation("preClassify")
        # self.AIThread.start()
        try:
            # 获取选择图片
            files, _ = QFileDialog.getOpenFileNames(self, "Open files",
                                                    u"./images/image_test",
                                                    "Image Files (*.jpg *.png *.gif *.bmp *.jpeg, *.tif, *.Webp)")
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
            NotificationWindow.error(self, "警告", "请<b><u>选择一个有效路径</u></b>", callback=self._getBatchImage)

    def __classifyBatchImages(self):
        if len(self.files) == 0:
            NotificationWindow.info(self, "注意", "请先进行<b><u>批量导入图片</u></b>", callback=self._getBatchImage)
            return
        # 每次进行预测时清空之前的预测结果
        self.barChartWidget.clearData()
        # AI线程启动批量预测
        print("AI Thread is running: classify")
        self.AIThread.setFiles(self.files)
        self.AIThread.setOperation("batchClassify")
        self.AIThread.start()
        self.statisticsTextEdit.setText("")
        # 禁用部分按钮
        self._lock_button()
        # 批量预测-进度条
        self.progressBar2.setMaximum(len(self.files))
        self.progressBar2.setValue(0)

    def __clearTableContent(self):
        NotificationWindow.info(self, "是否确认",
                                "<font color=red><b><u>清除已导入图片</u></b></font>",
                                callback=self.__clearTable)

    def __clearTable(self):
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
        if not os.path.exists(path):
            NotificationWindow.warning(self, "注意",
                                       "请先<font color=blue><b><u>选择正确的导出路径</u></b></font>",
                                       callback=self._exportBatchImages)
            return
        count = self.tableWidget.rowCount()
        if count == 0:
            NotificationWindow.warning(self, "注意", "请先<b><u>导入图片</u></b>进行图片预测", callback=self.__classifyBatchImages)
            return
        print("AI Thread is running: batch export")
        self.AIThread.setOperation("batchExport")
        self.AIThread.start()
        self._lock_button()

    def _lock_button(self):
        self.my_cursor.startBusy()
        self.menu_M.setEnabled(False)
        self.actionClassify.setEnabled(False)
        self.predictButton.setEnabled(False)
        self.batchPredictButton.setEnabled(False)
        self.batchExportButton.setEnabled(False)
        self.batchChooseButton.setEnabled(False)
        self.clearTableButton.setEnabled(False)

    def _release_button(self):
        self.my_cursor.stopBusy()
        self.menu_M.setEnabled(True)
        self.actionClassify.setEnabled(True)
        self.predictButton.setEnabled(True)
        self.batchPredictButton.setEnabled(True)
        self.batchExportButton.setEnabled(True)
        self.batchChooseButton.setEnabled(True)
        self.clearTableButton.setEnabled(True)

    def _saveImage(self):
        if self.flower_pixmap is None:
            NotificationWindow.info(self, "注意",
                                    "请先<font color=blue><b><u>导入图片</u></b></font>",
                                    callback=self._getImage)
            return
        self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
        img = self.flower_image  # 副本操作
        image_name = self.flower_name
        if self.saveNameEdit.text() is not None:
            image_name = self.saveNameEdit.text()
        try:
            save_path = self.savePathTextEdit.toPlainText()
        except AttributeError:
            NotificationWindow.error(self, "错误", "请先<font color=blue><b><u>选择保存路径</u></b></font>",
                                     callback=self.getDirectory)
            return
        if not os.path.exists(save_path):
            NotificationWindow.error(self, "错误",
                                     "请输入或<font color=blue><b><u>选择正确的文件夹地址</u></b>",
                                     callback=self.getDirectory)
            # QMessageBox.information(self, "错误", "请选择正确的文件夹地址")
            return
        save_path = save_path + "/" + image_name  # 拼接保存路径：文件夹+文件原始名称
        # 进行扩展名操作
        extend_name = self.comboBox.currentText()
        if extend_name != "默认扩展名" and extend_name != "":
            # 非默认或未选状态（选择了某个扩展名）：进行扩展名修改
            extend_name = extend_name.split(".")[-1]
            save_path = save_path.split(".")[0] + "." + extend_name
        # 进行色彩模式操作
        color_mode = self.comboBox_2.currentText()
        if color_mode != "默认色彩模式" and color_mode != "":
            # 非默认或未选状态（选择了某个色彩模式）：进行色彩模式修改
            img = img.convert(color_mode)
            print("color mode:", img.mode)
        # 进行分辨率操作
        height = self.spinBox_height.value()
        width = self.spinBox_width.value()
        if height != 0 and width != 0:
            img = img.resize((height, width), Image.ANTIALIAS)
        try:
            img.save(save_path, format=extend_name)
        except Exception as e:
            print(e)
            try:
                os.remove(save_path)  # 尝试删除创建失败的临时文件
            except Exception as e:
                print(e)
                pass
            NotificationWindow.error(
                self, "错误",
                "请输入或选择正确的文件扩展名(*.jpg *.png *.gif *.bmp *.jpeg, *.tif, *.Webp ...)")
            return
        NotificationWindow.success(self, "保存成功", f"文件路径：<font color=blue><u>{save_path}</u></font>",
                                   # 打开所在文件夹并选中该文件
                                   callback=lambda: os.system(f'explorer /select, "{pathlib.Path(save_path)}'))

    def __changeComboBox(self, text):
        if text == "RGBA":
            self.disable_item_comboBox(self.comboBox, [1], 0)
            self.disable_item_comboBox(self.comboBox, [2, 3, 4, 5, 6], 1 | 32)
        elif text == "HSV":
            self.disable_item_comboBox(self.comboBox, [1, 2, 3, 4, 5], 0)
            self.disable_item_comboBox(self.comboBox, [6], 1 | 32)
        elif text == "CMYK":
            self.disable_item_comboBox(self.comboBox, [2, 3, 4], 0)
            self.disable_item_comboBox(self.comboBox, [1, 5, 6], 1 | 32)
        elif text == "1" or text == "L" or text == "RGB" or text == "默认色彩模式":
            self.disable_item_comboBox(self.comboBox, [1, 2, 3, 4, 5, 6], 1 | 32)
        if text == "jpeg":
            self.disable_item_comboBox(self.comboBox_2, [4, 5], 0)
            self.disable_item_comboBox(self.comboBox_2, [1, 2, 3, 6], 1 | 32)
        elif text == "png" or text == "bmp" or text == "gif":
            self.disable_item_comboBox(self.comboBox_2, [5, 6], 0)
            self.disable_item_comboBox(self.comboBox_2, [1, 2, 3, 4], 1 | 32)
        elif text == "tiff":
            self.disable_item_comboBox(self.comboBox_2, [5], 0)
            self.disable_item_comboBox(self.comboBox_2, [1, 2, 3, 4, 6], 1 | 32)
        elif text == "Webp" or text == "默认扩展名":
            self.disable_item_comboBox(self.comboBox_2, [1, 2, 3, 4, 5, 6], 1 | 32)

    @staticmethod
    def disable_item_comboBox(combo_box: QComboBox, operation_list: list, v=0):
        """
        将下拉按钮中的某些项目批量禁用
        :param combo_box: comboBox对象
        :param operation_list: 需要禁用的项目,列表数据,如[1,2,5,6]
        :param v: 0为禁用,1|32为解除
        """
        for i in range(len(operation_list)):
            index = combo_box.model().index(operation_list[i], 0)  # 选择需要设定的项目
            combo_box.model().setData(index, v, Qt.UserRole - 1)  # 禁用comboBox的指定项目

    def __dropImage(self, tag: bool, url: str, pixmap: QPixmap):
        """
        tag: 标识是否为浏览器文件
        url: 图片的url(本地地址和浏览器链接)
        """
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
            NotificationWindow.info(self, "注意",
                                    "请先<font color=blue><b><u>导入图片</u></b></font>",
                                    callback=self._getImage)
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
        file_path = self.tableWidget.item(row, 0).text() + "/" + self.tableWidget.item(row, 1).text()
        self.image_viewer = ImageViewer(image=file_path, background=QColor(235, 255, 244))
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

    def __menu_style_operation(self, action):
        if action == self.actionMyStyle:
            self.setStyleSheet(readQssFile(u"./stylesheet/style.qss"))
            self.actionMyStyle.setChecked(True)
        else:
            self.actionMyStyle.setChecked(False)
        if action == self.actionUbuntuStyle:
            self.setStyleSheet(readQssFile(u"./stylesheet/Ubuntu.qss"))
            self.actionUbuntuStyle.setChecked(True)
        else:
            self.actionUbuntuStyle.setChecked(False)
        if action == self.actionAMOLED:
            self.setStyleSheet(readQssFile(u"./stylesheet/AMOLED.qss"))
            self.actionAMOLED.setChecked(True)
        else:
            self.actionAMOLED.setChecked(False)
        if action == self.actionAqua:
            self.setStyleSheet(readQssFile(u"./stylesheet/Aqua.qss"))
            self.actionAqua.setChecked(True)
        else:
            self.actionAqua.setChecked(False)
        if action == self.actionConsoleStyle:
            self.setStyleSheet(readQssFile(u"./stylesheet/ConsoleStyle.qss"))
            self.actionConsoleStyle.setChecked(True)
        else:
            self.actionConsoleStyle.setChecked(False)
        if action == self.actionElegantDark:
            self.setStyleSheet(readQssFile(u"./stylesheet/ElegantDark.qss"))
            self.actionElegantDark.setChecked(True)
        else:
            self.actionElegantDark.setChecked(False)
        if action == self.actionMacOS:
            self.setStyleSheet(readQssFile(u"./stylesheet/MacOS.qss"))
            self.actionMacOS.setChecked(True)
        else:
            self.actionMacOS.setChecked(False)
        if action == self.actionManjaroMix:
            self.setStyleSheet(readQssFile(u"./stylesheet/ManjaroMix.qss"))
            self.actionManjaroMix.setChecked(True)
        else:
            self.actionManjaroMix.setChecked(False)
        if action == self.actionMaterialDark:
            self.setStyleSheet(readQssFile(u"./stylesheet/MaterialDark.qss"))
            self.actionMaterialDark.setChecked(True)
        else:
            self.actionMaterialDark.setChecked(False)

    def __toolBarOperation(self, action):
        if action == self.actionClassify:
            if self.flower_pixmap is None:
                NotificationWindow.error(self, "错误", "请先<b><u>导入图片</u></b>",
                                         callback=self._getImage)
            else:
                NotificationWindow.info(
                    self, "确认启动深度识别",
                    u'这需花费较长时间：<font color=red><b><u>确定</u></b></font>',
                    callback=self.__deepClassify)
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
        self.progressBar1.setMaximum(len(get_installed_model()[0]))
        self.horizontalLayout_3.addWidget(self.progressBar1)
        self.progressBar1.setValue(0)
        # 进行深度预测
        print("AI Thread is running: deepClassify")
        self.AIThread.setFiles(self.flower_pixmap)
        self.AIThread.setOperation("deepClassify")
        self.AIThread.start()
        # 禁用部分按钮
        self._lock_button()

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
                                                  "Image Files (*.jpg *.png *.gif *.bmp *.jpeg, *.tif, *.Webp)")
            if file:
                self.flower_path = file  # 获取文件地址
                self.directory_path, self.flower_name = os.path.split(file)  # 获取花朵文件名
                self.flower_pixmap = QPixmap(file)  # 获取花朵图片
                self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
                self.update()
        except FileNotFoundError:
            NotificationWindow.warning(self, "警告", "请选择一个有效路径", callback=self._getImage)

    def __resetImage(self):
        """
        槽函数
        重新导入工作区的图片
        (不包括剪贴板临时图片)
        """
        try:
            if os.path.exists(self.flower_path):  # 如果是本地url，则直接重新读取重置
                self.flower_pixmap = QPixmap(self.flower_path)
            else:  # 如果不是本地url，则重置为drop时的pixmap
                self.flower_pixmap = QPixmap(self.imageLabel.my_pixmap)  # 重置QPixmap格式的flower
            self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)  # 更新Image格式的flower
            self.update()
            NotificationWindow.success(self, "成功", "已重置原图", time=3000)
        except TypeError as e:
            print(e)
            NotificationWindow.info(self, "注意", "请先<font color=blue><b><u>导入图片</u></b></font>", callback=self._getImage)

    def __classifyImage(self):
        """
        槽函数
        进行图片预测
        调用饼图绘制并加载详细信息
        """
        if self.flower_pixmap is None:
            NotificationWindow.info(self, "注意", "请先进行<b><u>批量导入图片</u></b>", callback=self._getBatchImage)
            return
        print("AI Thread is running: classify")
        self.AIThread.setFiles(self.flower_pixmap)
        self.AIThread.setOperation("classify")
        self.AIThread.start()
        # 禁用部分按钮
        self._lock_button()

    def __showBarChartView(self):
        self.barChartWidget.show()

    def initStyleSheet(self):
        style = readQssFile(u"./stylesheet/Ubuntu.qss")
        self.actionUbuntuStyle.setChecked(True)
        self.setStyleSheet(style)

    def update(self):
        print("update")
        self.pathLabel.setText(self.directory_path)  # 更新显示文件夹地址
        self.pathLabel.setToolTip("双击打开")  # 更新显示文件夹地址提示
        self.nameEdit.setText(self.flower_name)  # 更新显示文件名
        self.imageLabel.setPixmap(self.flower_pixmap)  # 更新显示花朵图片
        self.resultLabel.setText("{}的预测结果：".format(self.flower_name))  # 更新预加载处理结果
        mode = "<p>色彩模式：<b>"
        print("real color mode:", self.flower_image.mode)
        for c in self.flower_image.mode:
            if c == 'R':
                mode += "<font color=red>R</font>"
            elif c == 'G':
                mode += "<font color=green>G</font>"
            elif c == 'B':
                mode += "<font color=blue>B</font>"
            elif c == 'A' or c == "K" or c == "1":
                mode += f"<font color=black>{c}</font>"
            elif c == 'C':
                mode += "<font color=aqua>C</font>"
            elif c == 'M':
                mode += "<font color=#8B008B>M</font>"
            elif c == 'Y':
                mode += "<font color=yellow>Y</font>"
            elif c == 'L':
                mode += "<font color=gray>L</font>"
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
        self.initPieChart()
        self.statusBar().showMessage("模型：" + self.ai_model.__class__.__name__)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressX = event.position().x()  # 记录鼠标按下的时候的坐标
            self.pressY = event.position().y()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.drag = True
        if event.button() == Qt.RightButton:
            # 主页面上下文菜单
            self.context_menu = QMenu(self)
            self.context_menu.addActions(self.menu_style.actions())
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.context_menu.exec(event.globalPosition().toPoint())

    def mouseMoveEvent(self, event):
        if self.drag:
            x = event.position().x()
            y = event.position().y()  # 获取移动后的坐标
            move_x = x - self.pressX
            move_y = y - self.pressY  # 计算移动了多少
            position_x = self.frameGeometry().x() + move_x
            position_y = self.frameGeometry().y() + move_y  # 计算移动后主窗口在桌面的位置
            self.move(position_x, position_y)  # 移动主窗口

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.drag = False

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


def get_installed_model() -> [list, set]:
    installed = []
    models_name = ["VGG19", "InceptionV3", "DenseNet121", "MobileNetV2", "EfficientNetB0",
                   "EfficientNetB2", "EfficientNetB4", "EfficientNetB7"]
    for model_name in models_name:
        checkpoint_save_path = "./checkpoint/flower_" + model_name + ".ckpt"
        if os.path.exists(checkpoint_save_path + '.index'):
            installed.append(model_name)
    return installed, set(models_name) - set(installed)


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
