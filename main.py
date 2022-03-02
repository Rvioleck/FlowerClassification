import shutil
import sys

from PIL import ImageGrab
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtCore import QEvent, QPoint
from PySide6.QtGui import QAction, QPen, Qt, QPainter, QIcon, QColor, QCursor, QKeySequence, QShortcut, QImage
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication, QTableWidgetItem, QMenu

from AIModel.cnn_models import *
from AIModel.data_process import *
from ImageCutter import Form
from ImageViewer import ImageViewer
from ui_MainWindowFlower import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.flower_path = ""
        self.flower_image = None
        self.batchDirectory = ""  # 记录批量图片保存路径
        self.files = []  # 记录已选中的批量图片路径
        self.setupUi(self)  # GUI界面初始化(Viewer)
        self.initUI()  # 业务操作初始化(Controller)
        self.initModel()  # AI模型初始化(Model)

    def initModel(self):
        self.ai_model = MyModel()  # 设置默认模型
        load_model(self.ai_model)  # 加载模型权值

    def initUI(self):
        # 绑定按钮点击信号
        self.chooseButton.clicked.connect(self.getImage)
        self.batchChooseButton.clicked.connect(self.getBatchImage)
        self.predictButton.clicked.connect(self.predictImage)
        self.clearTableButton.clicked.connect(self.clearTableContent)
        self.batchPredictButton.clicked.connect(self.batchPredictImages)
        self.getDirectoryButton.clicked.connect(self.getDirectory)
        self.batchExportButton.clicked.connect(self.batchExportImages)
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
        # self.twPopMenu.triggered.connect(self.deleteRow)  # 绑定菜单行为的槽
        self.delAction.triggered.connect(self.deleteRow)  # 绑定"删除行为"的槽
        # label预加载
        self.batchImportLabel.setText("已加载图片张数：{}".format(len(self.files)))
        # 应用程序全局热键
        QShortcut(QKeySequence(self.tr("Ctrl+V")), self, self.pasteImage)

    def getDirectory(self):
        self.batchDirectory = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                               "D:\\AI_LEARNING_PDF\\deep learning\\flower_images")
        self.savePathLineEdit.setText(self.batchDirectory)

    def batchExportImages(self):
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
        self.statusBar().showMessage("导出预测结果共{}张图片".format(count))
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
        if self.flower_path == "":  # 未导入图片则不进入函数
            return
        self.image_cutter = Form(image=self.flower_path)
        self.image_cutter.save_signal.connect(self.passImage)
        self.image_cutter.show()

    def viewImage(self, row):
        print(self.files[row])
        self.image_viewer = ImageViewer(image=self.files[row], background=QColor(28, 31, 34))
        self.image_viewer.show()

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
        except Exception as e:
            print(e)

    def menuOperation(self, action):
        if action == self.actionNew:
            print("new")
        elif action == self.actionOpen:
            self.getImage()
        elif action == self.actionClose:
            app.exit()

    def eventFilter(self, watched, event) -> bool:
        # 过滤器实现label点击事件
        if watched == self.imageLabel:
            if event.type() == QEvent.MouseButtonDblClick:
                self.getImage()
        # 对于其余情况返回默认处理方法
        return QMainWindow.eventFilter(self, watched, event)

    def chooseModel(self, model_action):
        pre_model = self.ai_model
        if model_action == self.myModelAction:
            self.ai_model = MyModel()
        elif model_action == self.denseNet121Action:
            self.ai_model = DenseNet121()
        elif model_action == self.resNetAction:
            self.ai_model = ResNet18([2, 2, 2, 2])
        elif model_action == self.alexNetAction:
            self.ai_model = AlexNet8()
        elif model_action == self.inceptionAction:
            self.ai_model = InceptionV3()
        elif model_action == self.vggAction:
            self.ai_model = VGG19()
        elif model_action == self.mobileNetAction:
            self.ai_model = MobileNetV2()
        if model_action != self.actionCNN:
            if load_model(self.ai_model):
                QMessageBox.information(self, "成功",
                                        "成功导入模型" + self.ai_model.__class__.__name__,
                                        QMessageBox.Ok)
                self.statusBar().showMessage("模型：" + self.ai_model.__class__.__name__)
                self.resultLabel.setText(self.resultLabel.text().split("：")[0] + "：")
            else:
                self.ai_model = pre_model
                QMessageBox.warning(self, "错误",
                                    "未导入模型" + self.ai_model.__class__.__name__,
                                    QMessageBox.Ok)
        else:
            self.showStatistics()

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
        try:
            file, a = QFileDialog.getOpenFileName(self, "Open file",
                                                  "D:\\AI_LEARNING_PDF\\deep learning\\flower_images",
                                                  "Image Files (*.jpg *.png)")
            if file:
                self.flower_path = file
                directory_path, self.flower_name = os.path.split(file)  # 获取花朵文件名
                self.flower_pixmap = QPixmap(file)  # 获取花朵图片
                # size = self.flower_image.size()
                # self.imageLabel.resize(size)
                self.pathLabel.setText(directory_path)
                self.nameEdit.setText(self.flower_name)
                self.imageLabel.setPixmap(self.flower_pixmap)
                self.resultLabel.setText("{}的预测结果：".format(self.flower_name))
                self.flower_image = ImageQt.fromqpixmap(self.flower_pixmap)
                self.imageTextEdit.setText(
                    "<p>图片分辨率：<b><font color=red>{}×{}</font></b></p>"
                    "<p>图片格式：<b><font color=red>{}</font></b></p>"
                    "<p>色彩模式：<b><font color=red>{}</font></b></p>".format(
                        self.flower_image.size[0], self.flower_image.size[1], self.flower_image.format,
                        self.flower_image.mode))
        except FileNotFoundError:
            QMessageBox.warning(self, "警告", "请选择一个有效路径", QMessageBox.Ok)

    def resetImage(self):
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

    def clearTableContent(self):
        res = QMessageBox.information(self, "确认", "是否清除已导入图片",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.tableWidget.setRowCount(0)
            self.tableWidget.clearContents()
            self.files.clear()

    def getBatchImage(self):
        try:
            files, a = QFileDialog.getOpenFileNames(self, "Open files",
                                                    "D:\\AI_LEARNING_PDF\\deep learning\\flower_images",
                                                    "Image Files (*.jpg *.png *.jpeg *.gif)")
            num = len(files)
            row_count = self.tableWidget.rowCount()
            for i in range(num):
                file = files[i]
                img_path, img_name = os.path.split(file)
                self.tableWidget.insertRow(row_count + i)
                self.tableWidget.setItem(row_count + i, 0, QTableWidgetItem(img_path))
                self.tableWidget.setItem(row_count + i, 1, QTableWidgetItem(img_name))
                self.tableWidget.setItem(row_count + i, 2, QTableWidgetItem(""))

            # self.statusBar().showMessage("加载图片" + str(num + row_count) + "张")
            self.files.extend(files)
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "警告", "请选择一个有效路径", QMessageBox.Ok)

    def predictImage(self):
        # self.resultLabel.setText("正在分析中...")
        # if self.flower_path == "":  # 未导入图片则不进入函数
        #     return
        portion, res, index = model_predict(model=self.ai_model, image=self.flower_pixmap)
        prompt = "{}的预测结果：<b><font color=red>{}</font></b>".format(self.flower_name, res)
        self.resultLabel.setText(prompt)
        self.drawPieChart(portion, index)

    def batchPredictImages(self):
        for i, file in enumerate(self.files):
            pixmap = QPixmap(file)
            _, res, _ = model_predict(self.ai_model, pixmap)
            icon_path = u"images/flowers/{}.png".format(res)
            self.tableWidget.setItem(i, 2, QTableWidgetItem(QIcon(icon_path), res))

    def showStatistics(self):
        # 展示模型统计
        model_name = self.ai_model.__class__.__name__
        history_show(model_name)

    def drawPieChart(self, portion, index):
        colors = [(255, 148, 217), (241, 203, 6), (96, 67, 1), (187, 187, 187),
                  (227, 58, 91), (169, 177, 232), (153, 69, 253), (176, 197, 122),
                  (106, 135, 89), (28, 77, 183), (224, 189, 213), (189, 115, 121),
                  (195, 195, 136), (120, 0, 20), (205, 134, 18), (240, 96, 140)]
        series = QPieSeries()
        series.append("叶子花", portion[0])
        series.append("雏菊", portion[1])
        series.append("蒲公英", portion[2])
        series.append("栀子花", portion[3])
        series.append("木槿花", portion[4])
        series.append("绣球花", portion[5])
        series.append("鸢尾花", portion[6])
        series.append("百合花", portion[7])
        series.append("荷花", portion[8])
        series.append("牵牛花", portion[9])
        series.append("桃花", portion[10])
        series.append("牡丹花", portion[11])
        series.append("蝴蝶兰", portion[12])
        series.append("玫瑰花", portion[13])
        series.append("向日葵", portion[14])
        series.append("郁金香", portion[15])
        for i, slice in enumerate(series.slices()):
            slice.setColor(QColor(colors[i][0], colors[i][1], colors[i][2]))
            slice.setBorderColor(QColor(colors[i][0], colors[i][1], colors[i][2]))
            slice.setLabelColor(QColor(colors[i][0], colors[i][1], colors[i][2]))
            slice.setLabelArmLengthFactor(0.2)
        # 这里要处理的是python项，是依据前面append的顺序，如果是处理C++项的话，那索引就是3
        slice = series.slices()[index]
        # 突出显示，设置颜色
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkBlue, 2))
        # slice.setBrush(Qt.red)
        for i in range(0, 16):
            if i == index:
                continue
            if portion[i] > 0.03:
                this_slice = series.slices()[i]
                this_slice.setLabelVisible(True)
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
        except Exception as e:
            print(e)
        # 创建ChartView，它是显示图表的控件
        self.pieWidget = QChartView(chart)
        self.pieWidget.setRenderHint(QPainter.Antialiasing)
        self.pieWidget.isVisible()
        self.verticalLayout_2.addWidget(self.pieWidget)
        # self.setCentralWidget(self.pieWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec())
