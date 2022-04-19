# -*- coding: utf-8 -*-
import numpy as np
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QDialog, QTextEdit

from ui_my_convolutioner import Ui_Dialog


class ImageConvolutioner(QDialog, Ui_Dialog):
    save_signal = Signal(QPixmap)

    def __init__(self, parent, image: QPixmap, name=None):
        super(ImageConvolutioner, self).__init__()
        self.image = image
        self.new_image = QPixmap(image)
        self.rgb = self.get_RGB_matrix(image)
        self.setupUi(self)
        self.init_ui()
        self.main_window = parent
        # 视图背景颜色
        self.setWindowTitle(f"图片卷积操作 --- {name}")
        self.initConnectSlot()

    def init_ui(self):
        self.orginImage.setPixmap(self.image)

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

    def eventFilter(self, watched, event) -> bool:
        pass
        # if watched == self.brightness_label:
        #     if event.type() == QEvent.MouseButtonDblClick:
        #         self.horizontalSliderBrightness.setValue(0)
        # if watched == self.contrast_label:
        #     if event.type() == QEvent.MouseButtonDblClick:
        #         self.horizontalSliderContrast.setValue(0)
        # if watched == self.hue_label:
        #     if event.type() == QEvent.MouseButtonDblClick:
        #         self.horizontalSliderHues.setValue(0)
        # if watched == self.saturation_label:
        #     if event.type() == QEvent.MouseButtonDblClick:
        #         self.horizontalSliderSaturation.setValue(0)
        # return QDialog.eventFilter(self, watched, event)
