from PySide6.QtCore import QSize, Qt, QRect, Signal, QPointF
from PySide6.QtGui import QColor, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox, \
    QToolButton, QDial

from my_graphics import GraphicsView


class ImageCutter(QDialog):
    save_signal = Signal(QPixmap)

    def __init__(self, image):
        super(ImageCutter, self).__init__()
        self.resize(1024, 768)
        self.image = image
        self.init_ui()
        window_icon = QIcon()
        window_icon.addFile(u"images/花朵(1).png")
        self.setWindowIcon(window_icon)
        # self.setupUi(self)
        # 视图背景颜色
        self.setWindowTitle("图片裁剪")
        self.graphicsView.save_signal.connect(self.savePushButton.setEnabled)
        self.cutPushButton.clicked.connect(self.pushButton_cut_clicked)
        self.savePushButton.clicked.connect(self.pushButton_save_clicked)
        self.rightRotateToolButton.clicked.connect(self.rightRotateToolButton_clicked)
        self.leftRotateToolButton.clicked.connect(self.leftRotateToolButton_clicked)
        self.horizontalFlipToolButton.clicked.connect(self.horizontalFlipToolButton_clicked)
        self.verticalFlipToolButton.clicked.connect(self.verticalFlipToolButton_clicked)
        self.rotationDial.valueChanged.connect(self.rotationDial_valueChanged)

    def init_ui(self):
        self.cutPushButton = QPushButton(self)
        self.cutPushButton.setObjectName(u"putButton_cut")
        self.cutPushButton.setGeometry(QRect(790, 707, 41, 41))
        icon = QIcon()
        icon.addFile(u"images/\u7f16\u8f91\u56fe\u7247.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cutPushButton.setIcon(icon)
        self.cutPushButton.setIconSize(QSize(32, 32))
        self.cutPushButton.setCheckable(True)
        self.cutPushButton.setFlat(True)
        self.savePushButton = QPushButton(self)
        self.savePushButton.setText("确定")
        self.savePushButton.setObjectName(u"putButton_save")
        self.savePushButton.setEnabled(False)
        self.savePushButton.setGeometry(QRect(880, 710, 91, 31))

        self.graphicsView = GraphicsView(self.image, self)
        self.graphicsView.setBackgroundBrush(QColor(235, 255, 244))
        self.graphicsView.setGeometry(QRect(0, 0, 1021, 691))
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.rightRotateToolButton = QToolButton(self)
        self.rightRotateToolButton.setText("顺时针旋转")
        self.rightRotateToolButton.setObjectName(u"rightRotateToolButton")
        self.rightRotateToolButton.setGeometry(QRect(50, 700, 71, 61))
        icon1 = QIcon()
        icon1.addFile(u"images/\u53f3\u65cb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightRotateToolButton.setIcon(icon1)
        self.rightRotateToolButton.setIconSize(QSize(36, 36))
        self.rightRotateToolButton.setCheckable(False)
        self.rightRotateToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.rightRotateToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.rightRotateToolButton.setAutoRaise(True)
        self.leftRotateToolButton = QToolButton(self)
        self.leftRotateToolButton.setText("逆时针旋转")
        self.leftRotateToolButton.setObjectName(u"leftRotateToolButton")
        self.leftRotateToolButton.setGeometry(QRect(180, 700, 71, 61))
        icon2 = QIcon()
        icon2.addFile(u"images/\u5de6\u65cb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftRotateToolButton.setIcon(icon2)
        self.leftRotateToolButton.setIconSize(QSize(36, 36))
        self.leftRotateToolButton.setCheckable(False)
        self.leftRotateToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.leftRotateToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.leftRotateToolButton.setAutoRaise(True)
        self.horizontalFlipToolButton = QToolButton(self)
        self.horizontalFlipToolButton.setText("水平翻转")
        self.horizontalFlipToolButton.setObjectName(u"horizontalFlipToolButton")
        self.horizontalFlipToolButton.setGeometry(QRect(400, 700, 71, 61))
        icon3 = QIcon()
        icon3.addFile(u"images/\u6c34\u5e73\u7ffb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.horizontalFlipToolButton.setIcon(icon3)
        self.horizontalFlipToolButton.setIconSize(QSize(36, 36))
        self.horizontalFlipToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.horizontalFlipToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.horizontalFlipToolButton.setAutoRaise(True)
        self.verticalFlipToolButton = QToolButton(self)
        self.verticalFlipToolButton.setText("垂直翻转")
        self.verticalFlipToolButton.setObjectName(u"verticalFlipToolButton")
        self.verticalFlipToolButton.setGeometry(QRect(310, 700, 71, 61))
        icon4 = QIcon()
        icon4.addFile(u"images/\u5782\u76f4\u7ffb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verticalFlipToolButton.setIcon(icon4)
        self.verticalFlipToolButton.setIconSize(QSize(36, 36))
        self.verticalFlipToolButton.setCheckable(False)
        self.verticalFlipToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.verticalFlipToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.verticalFlipToolButton.setAutoRaise(True)
        self.rotationDial = QDial(self)
        self.rotationDial.setObjectName(u"rotationDial")
        self.rotationDial.setGeometry(QRect(125, 700, 50, 50))
        self.rotationDial.setMaximum(360)
        self.rotationDial.setSingleStep(5)
        self.rotationDial.setPageStep(20)
        self.rotationDial.setInvertedAppearance(False)
        self.rotationDial.setInvertedControls(False)
        self.rotationDial.setWrapping(True)
        self.rotationDial.setNotchesVisible(True)

        self.savePushButton.setStyleSheet(u"QPushButton\n"
                                          "{\n"
                                          "    color:white;\n"
                                          "    background-color:rgb(14 , 150 , 254);\n"
                                          "    border-radius:5px;\n"
                                          "}\n"
                                          " \n"
                                          "QPushButton:hover\n"
                                          "{\n"
                                          "    color:white;\n"
                                          "    background-color:rgb(44 , 137 , 255);\n"
                                          "}\n"
                                          " \n"
                                          "QPushButton:pressed\n"
                                          "{\n"
                                          "    color:white;\n"
                                          "    background-color:rgb(14 , 135 , 228);\n"
                                          "    padding-left:3px;\n"
                                          "    padding-top:3px;\n"
                                          "}\n"
                                          "")

    def pushButton_cut_clicked(self):
        if self.graphicsView.image_item.is_start_cut:
            self.graphicsView.image_item.is_start_cut = False
            self.graphicsView.image_item.setCursor(Qt.ArrowCursor)  # 箭头光标
        else:
            self.graphicsView.image_item.is_start_cut = True
            self.graphicsView.image_item.setCursor(Qt.CrossCursor)  # 十字光标

    def pushButton_save_clicked(self):
        try:
            start_point = QPointF(
                min(self.graphicsView.image_item.start_point.x(), self.graphicsView.image_item.end_point.x()),
                min(self.graphicsView.image_item.start_point.y(), self.graphicsView.image_item.end_point.y())
            )
            end_point = QPointF(
                max(self.graphicsView.image_item.start_point.x(), self.graphicsView.image_item.end_point.x()),
                max(self.graphicsView.image_item.start_point.y(), self.graphicsView.image_item.end_point.y()))
            rect = QRect(start_point.toPoint(), end_point.toPoint())
            cropped_pixmap = self.graphicsView.image_item.pixmap().copy(rect)
            self.save_signal.emit(cropped_pixmap)
            QMessageBox.information(self, "完成", "裁剪完成！", QMessageBox.Ok)
        except AttributeError as e:
            print(e)
            print("进行裁剪操作未裁剪")
        self.close()

    def rightRotateToolButton_clicked(self):
        self.graphicsView.img_signal.emit(0)

    def leftRotateToolButton_clicked(self):
        self.graphicsView.img_signal.emit(1)

    def horizontalFlipToolButton_clicked(self):
        self.graphicsView.img_signal.emit(2)

    def verticalFlipToolButton_clicked(self):
        self.graphicsView.img_signal.emit(3)

    def rotationDial_valueChanged(self):
        self.graphicsView.img_rotation_signal.emit(self.rotationDial.value())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = ImageCutter("test.png")
    form.show()
    app.exec()
