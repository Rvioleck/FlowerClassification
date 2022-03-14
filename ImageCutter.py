from PySide6.QtCore import Qt, QRect, Signal, QPointF
from PySide6.QtGui import QColor, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from my_graphics import GraphicsView
from ui_my_cutter import Ui_Dialog


class ImageCutter(QDialog, Ui_Dialog):
    save_signal = Signal(QPixmap)

    def __init__(self, image):
        super(ImageCutter, self).__init__()
        self.image = image
        self.setupUi(self)
        self.init_ui()
        # 视图背景颜色
        self.setWindowTitle("图片裁剪")
        self.initConnectSlot()

    def init_ui(self):
        window_icon = QIcon()
        window_icon.addFile(u"images/花朵(1).png")
        self.setWindowIcon(window_icon)
        self.cutPushButton.setStyleSheet(u"QPushButton{image: url(images/图片剪切.png);}\n"
                                         u"QPushButton:hover{image: url(images/图片剪切.png);}\n"
                                         u"QPushButton:pressed{image: url(images/剪切.png); padding: 3px}")

        self.graphicsView = GraphicsView(self.image, self)
        self.graphicsView.setBackgroundBrush(QColor(235, 255, 244))
        self.graphicsView.setGeometry(QRect(0, 0, 1021, 691))
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def initConnectSlot(self):
        self.graphicsView.save_signal.connect(self.savePushButton.setEnabled)
        self.cutPushButton.clicked.connect(self.pushButton_cut_clicked)
        self.savePushButton.clicked.connect(self.pushButton_save_clicked)
        self.rightRotateToolButton.clicked.connect(self.rightRotateToolButton_clicked)
        self.leftRotateToolButton.clicked.connect(self.leftRotateToolButton_clicked)
        self.horizontalFlipToolButton.clicked.connect(self.horizontalFlipToolButton_clicked)
        self.verticalFlipToolButton.clicked.connect(self.verticalFlipToolButton_clicked)
        self.rotationDial.valueChanged.connect(self.rotationDial_valueChanged)
        self.horizontalSliderBrightness.valueChanged.connect(self.horizontalSliderBrightness_valueChanged)
        self.horizontalSliderContrast.valueChanged.connect(self.horizontalSliderContrast_valueChanged)
        # self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        # self.pix = QBitmap("images/mask.png")
        # self.setMask(self.pix)

    def pushButton_cut_clicked(self):
        if self.graphicsView.image_item.is_start_cut:
            self.graphicsView.image_item.is_start_cut = False
            self.graphicsView.image_item.setCursor(Qt.OpenHandCursor)  # 箭头光标
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

    def horizontalSliderBrightness_valueChanged(self):
        self.graphicsView.img_brightness_signal.emit(self.horizontalSliderBrightness.value()/200)
        self.horizontalSliderContrast.setValue(0)

    def horizontalSliderContrast_valueChanged(self):
        self.graphicsView.img_contrast_signal.emit(self.horizontalSliderContrast.value())
        self.horizontalSliderBrightness.setValue(0)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = ImageCutter("./images/image_test/flowers (1).jpg")
    form.show()
    app.exec()
