# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'framelessDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_frameless_dialog(object):
    def setupUi(self, frameless_dialog):
        if not frameless_dialog.objectName():
            frameless_dialog.setObjectName(u"frameless_dialog")
        frameless_dialog.resize(403, 317)
        self.pushButton = QPushButton(frameless_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(167, 265, 75, 24))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton = QRadioButton(frameless_dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(47, 266, 95, 20))
        self.radioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.EfficientNetB0 = QCheckBox(frameless_dialog)
        self.EfficientNetB0.setObjectName(u"EfficientNetB0")
        self.EfficientNetB0.setGeometry(QRect(38, 103, 171, 20))
        self.EfficientNetB0.setCursor(QCursor(Qt.ArrowCursor))
        self.VGG19 = QCheckBox(frameless_dialog)
        self.VGG19.setObjectName(u"VGG19")
        self.VGG19.setGeometry(QRect(211, 223, 171, 20))
        self.VGG19.setCursor(QCursor(Qt.ArrowCursor))
        self.EfficientNetB1 = QCheckBox(frameless_dialog)
        self.EfficientNetB1.setObjectName(u"EfficientNetB1")
        self.EfficientNetB1.setGeometry(QRect(38, 133, 171, 20))
        self.EfficientNetB1.setCursor(QCursor(Qt.ArrowCursor))
        self.MobileNetV2 = QCheckBox(frameless_dialog)
        self.MobileNetV2.setObjectName(u"MobileNetV2")
        self.MobileNetV2.setGeometry(QRect(211, 133, 171, 20))
        self.MobileNetV2.setCursor(QCursor(Qt.ArrowCursor))
        self.EfficientNetB7 = QCheckBox(frameless_dialog)
        self.EfficientNetB7.setObjectName(u"EfficientNetB7")
        self.EfficientNetB7.setGeometry(QRect(211, 103, 171, 20))
        self.EfficientNetB7.setCursor(QCursor(Qt.ArrowCursor))
        self.EfficientNetB3 = QCheckBox(frameless_dialog)
        self.EfficientNetB3.setObjectName(u"EfficientNetB3")
        self.EfficientNetB3.setGeometry(QRect(38, 193, 171, 20))
        self.EfficientNetB3.setCursor(QCursor(Qt.ArrowCursor))
        self.DenseNet121 = QCheckBox(frameless_dialog)
        self.DenseNet121.setObjectName(u"DenseNet121")
        self.DenseNet121.setGeometry(QRect(211, 163, 171, 20))
        self.DenseNet121.setCursor(QCursor(Qt.ArrowCursor))
        self.EfficientNetB2 = QCheckBox(frameless_dialog)
        self.EfficientNetB2.setObjectName(u"EfficientNetB2")
        self.EfficientNetB2.setGeometry(QRect(38, 163, 171, 20))
        self.EfficientNetB2.setCursor(QCursor(Qt.ArrowCursor))
        self.EfficientNetB4 = QCheckBox(frameless_dialog)
        self.EfficientNetB4.setObjectName(u"EfficientNetB4")
        self.EfficientNetB4.setGeometry(QRect(38, 223, 171, 20))
        self.EfficientNetB4.setCursor(QCursor(Qt.ArrowCursor))
        self.InceptionV3 = QCheckBox(frameless_dialog)
        self.InceptionV3.setObjectName(u"InceptionV3")
        self.InceptionV3.setGeometry(QRect(211, 193, 171, 20))
        self.InceptionV3.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(frameless_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(55, 32, 271, 61))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.toolButton = QToolButton(frameless_dialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(346, 266, 24, 22))
        icon = QIcon()
        icon.addFile(u"images/\u5173\u4e8e.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setAutoRaise(True)

        self.retranslateUi(frameless_dialog)

        QMetaObject.connectSlotsByName(frameless_dialog)
    # setupUi

    def retranslateUi(self, frameless_dialog):
        frameless_dialog.setWindowTitle(QCoreApplication.translate("frameless_dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("frameless_dialog", u"\u786e\u5b9a", None))
        self.radioButton.setText(QCoreApplication.translate("frameless_dialog", u"\u5168\u9009", None))
        self.EfficientNetB0.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB0\": 0.956", None))
        self.VGG19.setText(QCoreApplication.translate("frameless_dialog", u"\"VGG19\": 0.707", None))
        self.EfficientNetB1.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB1\": 0.959", None))
        self.MobileNetV2.setText(QCoreApplication.translate("frameless_dialog", u"\"MobileNetV2\": 0.927", None))
        self.EfficientNetB7.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB7\": 0.959", None))
        self.EfficientNetB3.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB3\": 0.946", None))
        self.DenseNet121.setText(QCoreApplication.translate("frameless_dialog", u"\"DenseNet121\": 0.909", None))
        self.EfficientNetB2.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB2\": 0.952", None))
        self.EfficientNetB4.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB4\": 0.947", None))
        self.InceptionV3.setText(QCoreApplication.translate("frameless_dialog", u"\"InceptionV3\": 0.898", None))
        self.label.setText(QCoreApplication.translate("frameless_dialog", u"<html><head/><body><p>\u8bf7\u9009\u62e9\u8fdb\u884c<span style=\" font-weight:700; color:#ff0000;\">\u591a\u7f51\u7edc\u6a21\u578b\u7efc\u5408\u9884\u6d4b</span>\u6240\u7528\u6a21\u578b</p><p>\u2014\u2014&quot;\u6a21\u578b\u540d&quot;\uff1a\u6d4b\u8bd5\u96c6\u5206\u7c7b\u51c6\u786e\u7387</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("frameless_dialog", u"<html><head/><body><p><span style=\" font-weight:700; color:#ff0000;\">\u591a\u7f51\u7edc\u6a21\u578b\u7efc\u5408\u9884\u6d4b</span></p><p>\u7b97\u6cd5\uff1a</p><p>\u4ee5<span style=\" text-decoration: underline;\">\u6d4b\u8bd5\u96c6\u5206\u7c7b\u51c6\u786e\u7387</span>\u4e3a\u6743\u91cd\u8fdb\u884c\u6bcf\u4e2a\u7f51\u7edc\u7684\u5355\u72ec\u5206\u7c7b\uff0c\u5e76\u4e14\u5728\u6bcf\u4e2a\u7f51\u7edc\u6a21\u578b\u7684\u7ed3\u675f\u9636\u6bb5\u663e\u793a\u5f53\u524d\u7684\u52a0\u6743\u7ed3\u679c</p><p>\u539f\u7406\uff1a</p><p>\u7531\u4e8e\u6bcf\u4e2a\u6a21\u578b\u5747\u4e0d\u80fd\u5b8c\u5168\u6b63\u786e\u7684\u8bc6\u522b\u6240\u6709\u7684\u5ba2\u89c2\u82b1\u6735\u56fe\u50cf\uff0c\u5e76\u4e14\u6bcf\u4e2a\u6a21\u578b\u5bf9\u82b1\u6735\u56fe\u50cf\u7684\u62bd\u8c61\u7279\u5f81\u63d0\u53d6\u4e0d\u5c3d\u76f8\u540c\uff0c\u56e0\u6b64\u901a\u8fc7\u8bad\u7ec3\u96c6\u5206\u7c7b\u52a0\u6743\u7684\u65b9\u5f0f\u8fdb\u884c\u7efc\u5408\u8bc6\u522b\u80fd\u591f\u6700\u5927\u7a0b\u5ea6\u7ed3\u5408\u4e0d\u540c\u7f51\u7edc\u6240\u8bad"
                        "\u7ec3\u7684\u62bd\u8c61\u7279\u5f81\uff0c\u663e\u8457\u63d0\u5347\u5206\u7c7b\u8bc6\u522b\u7684\u51c6\u786e\u7387</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

