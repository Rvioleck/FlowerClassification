# -*- coding: utf-8 -*-
import numpy as np
from PySide6.QtCore import Signal, Slot, QSize
from PySide6.QtGui import QPixmap, QColor, Qt, QCursor
from PySide6.QtWidgets import QDialog, QTextEdit, QGraphicsDropShadowEffect, QVBoxLayout, QWidget, QGridLayout, \
    QSpacerItem, QSizePolicy, QPushButton

from ui_my_convolutioner import Ui_Dialog

Stylesheet = """
#Custom_Widget {
    background: white;
    border-radius: 10px;
}

#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: white;
    background: red;
}

"""

class ImageConvolutioner(QDialog, Ui_Dialog):
    save_signal = Signal(QPixmap)

    def __init__(self, parent, image: QPixmap):
        super(ImageConvolutioner, self).__init__()
        self.image = image
        self.new_image = QPixmap(image)
        self.rgb = self.get_RGB_matrix(image)
        self.init_ui()
        self.setupUi(self)
        self.orginImage.setPixmap(self.image)
        self.main_window = parent
        self.initConnectSlot()
        self.initGraphicsShadow()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.95)
        self.setStyleSheet(Stylesheet+parent.styleSheet())

    def init_ui(self):
        layout = QVBoxLayout(self)
        # 重点： 这个widget作为背景和圆角
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout.addWidget(self.widget)

        # 在widget中添加ui
        layout = QGridLayout(self.widget)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        layout.addWidget(QPushButton(
            'r', self, clicked=self.accept, objectName='closeButton'), 0, 1)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum,
                                   QSizePolicy.Expanding), 1, 0)

    def initConnectSlot(self):
        self.pushButton.clicked.connect(self.conv_start)
        self.saveButton.clicked.connect(self.save_button_clicked)
        self.slide_button.clicked.connect(self.slide_button_clicked)
        self.gaosi_slide_button.clicked.connect(self.gaosi_slide_button_clicked)
        self.horizonal_button.clicked.connect(self.horizonal_button_clicked)
        self.vertical_button.clicked.connect(self.vertical_button_clicked)
        self.sharp_button.clicked.connect(self.sharp_button_clicked)
        self.ex_sharp_button.clicked.connect(self.ex_sharp_button_clicked)

        # 绑定卷积完成信号
        self.main_window.AIThread.conv_finish.connect(self.convolution_finished)

    def initGraphicsShadow(self):
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(5, 5)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.orginImage.setGraphicsEffect(effect_shadow)
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(5, 5)  # 偏移
        effect_shadow.setBlurRadius(10)  # 阴影半径
        effect_shadow.setColor(Qt.gray)
        self.convolutionImage.setGraphicsEffect(effect_shadow)

    def get_RGB_matrix(self, image: QPixmap):
        w, h = image.width(), image.height()
        r = np.zeros((w, h))
        g = np.zeros((w, h))
        b = np.zeros((w, h))
        image = image.toImage()
        for i in range(0, w):
            for j in range(0, h):
                pixel = image.pixel(i, j)
                r[i][j], g[i][j], b[i][j] = QColor(pixel).getRgb()[:-1]
        return r, g, b

    def conv_start(self):
        for child in self.findChildren(QTextEdit):  # type: QTextEdit
            if child.toPlainText() is "":
                self.convolutionImage.setPixmap(self.image)
                return
        matrix = np.zeros((3, 3))
        count = 1
        for i in range(3):
            for j in range(3):
                text_edit_name = f"textEdit_{count}"
                count += 1
                matrix[i][j] = eval(f"float(eval(self.{text_edit_name}.toPlainText()))")

        self.main_window.AIThread.setOperation("Conv")  # 设置线程操作
        self.main_window.AIThread.setRGB(self.rgb, matrix)  # 设置参数
        self.main_window.AIThread.start()  # 启动运算线程
        self.main_window._lock_button()  # 锁按钮，显示鼠标忙

    def convolution_finished(self, pixmap):
        self.new_image = pixmap
        self.convolutionImage.setPixmap(pixmap)
        self.main_window._release_button()  # 释放按钮，释放鼠标

    @Slot()
    def save_button_clicked(self):
        self.save_signal[QPixmap].emit(self.new_image)
        self.close()

    @Slot()
    def slide_button_clicked(self):
        for child in self.findChildren(QTextEdit):  # type: QTextEdit
            child.setText("1/9")

    @Slot()
    def gaosi_slide_button_clicked(self):
        self.textEdit_1.setText("1/16")
        self.textEdit_2.setText("1/8")
        self.textEdit_3.setText("1/16")
        self.textEdit_4.setText("1/8")
        self.textEdit_5.setText("1/4")
        self.textEdit_6.setText("1/8")
        self.textEdit_7.setText("1/16")
        self.textEdit_8.setText("1/8")
        self.textEdit_9.setText("1/16")

    @Slot()
    def horizonal_button_clicked(self):
        self.textEdit_1.setText("-1")
        self.textEdit_2.setText("0")
        self.textEdit_3.setText("1")
        self.textEdit_4.setText("-1")
        self.textEdit_5.setText("0")
        self.textEdit_6.setText("1")
        self.textEdit_7.setText("-1")
        self.textEdit_8.setText("0")
        self.textEdit_9.setText("1")

    @Slot()
    def vertical_button_clicked(self):
        self.textEdit_1.setText("-1")
        self.textEdit_2.setText("-1")
        self.textEdit_3.setText("-1")
        self.textEdit_4.setText("0")
        self.textEdit_5.setText("0")
        self.textEdit_6.setText("0")
        self.textEdit_7.setText("1")
        self.textEdit_8.setText("1")
        self.textEdit_9.setText("1")

    @Slot()
    def sharp_button_clicked(self):
        self.textEdit_1.setText("0")
        self.textEdit_2.setText("-1")
        self.textEdit_3.setText("0")
        self.textEdit_4.setText("-1")
        self.textEdit_5.setText("5")
        self.textEdit_6.setText("-1")
        self.textEdit_7.setText("0")
        self.textEdit_8.setText("-1")
        self.textEdit_9.setText("0")

    @Slot()
    def ex_sharp_button_clicked(self):
        self.textEdit_1.setText("-1")
        self.textEdit_2.setText("-1")
        self.textEdit_3.setText("-1")
        self.textEdit_4.setText("-1")
        self.textEdit_5.setText("9")
        self.textEdit_6.setText("-1")
        self.textEdit_7.setText("-1")
        self.textEdit_8.setText("-1")
        self.textEdit_9.setText("-1")

    def sizeHint(self):
        return QSize(self.size())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressX = event.position().x()  # 记录鼠标按下的时候的坐标
            self.pressY = event.position().y()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.drag = True

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
