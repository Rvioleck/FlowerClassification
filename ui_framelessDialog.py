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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_frameless_dialog(object):
    def setupUi(self, frameless_dialog):
        if not frameless_dialog.objectName():
            frameless_dialog.setObjectName(u"frameless_dialog")
        frameless_dialog.resize(403, 276)
        self.pushButton = QPushButton(frameless_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 223, 75, 24))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.layoutWidget = QWidget(frameless_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 56, 341, 151))
        self.layoutWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.EfficientNetB0 = QCheckBox(self.layoutWidget)
        self.EfficientNetB0.setObjectName(u"EfficientNetB0")
        self.EfficientNetB0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.EfficientNetB0, 0, 0, 1, 1)

        self.EfficientNetB7 = QCheckBox(self.layoutWidget)
        self.EfficientNetB7.setObjectName(u"EfficientNetB7")
        self.EfficientNetB7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.EfficientNetB7, 0, 1, 1, 1)

        self.EfficientNetB1 = QCheckBox(self.layoutWidget)
        self.EfficientNetB1.setObjectName(u"EfficientNetB1")
        self.EfficientNetB1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.EfficientNetB1, 1, 0, 1, 1)

        self.MobileNetV2 = QCheckBox(self.layoutWidget)
        self.MobileNetV2.setObjectName(u"MobileNetV2")
        self.MobileNetV2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.MobileNetV2, 1, 1, 1, 1)

        self.EfficientNetB2 = QCheckBox(self.layoutWidget)
        self.EfficientNetB2.setObjectName(u"EfficientNetB2")
        self.EfficientNetB2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.EfficientNetB2, 2, 0, 1, 1)

        self.DenseNet121 = QCheckBox(self.layoutWidget)
        self.DenseNet121.setObjectName(u"DenseNet121")
        self.DenseNet121.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.DenseNet121, 2, 1, 1, 1)

        self.EfficientNetB3 = QCheckBox(self.layoutWidget)
        self.EfficientNetB3.setObjectName(u"EfficientNetB3")
        self.EfficientNetB3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.EfficientNetB3, 3, 0, 1, 1)

        self.InceptionV3 = QCheckBox(self.layoutWidget)
        self.InceptionV3.setObjectName(u"InceptionV3")
        self.InceptionV3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.InceptionV3, 3, 1, 1, 1)

        self.EfficientNetB4 = QCheckBox(self.layoutWidget)
        self.EfficientNetB4.setObjectName(u"EfficientNetB4")
        self.EfficientNetB4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.EfficientNetB4, 4, 0, 1, 1)

        self.VGG19 = QCheckBox(self.layoutWidget)
        self.VGG19.setObjectName(u"VGG19")
        self.VGG19.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.VGG19, 4, 1, 1, 1)

        self.radioButton = QRadioButton(frameless_dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 224, 95, 20))

        self.retranslateUi(frameless_dialog)

        QMetaObject.connectSlotsByName(frameless_dialog)
    # setupUi

    def retranslateUi(self, frameless_dialog):
        frameless_dialog.setWindowTitle(QCoreApplication.translate("frameless_dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("frameless_dialog", u"\u786e\u5b9a", None))
        self.EfficientNetB0.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB0\": 0.956", None))
        self.EfficientNetB7.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB7\": 0.959", None))
        self.EfficientNetB1.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB1\": 0.959", None))
        self.MobileNetV2.setText(QCoreApplication.translate("frameless_dialog", u"\"MobileNetV2\": 0.927", None))
        self.EfficientNetB2.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB2\": 0.952", None))
        self.DenseNet121.setText(QCoreApplication.translate("frameless_dialog", u"\"DenseNet121\": 0.909", None))
        self.EfficientNetB3.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB3\": 0.946", None))
        self.InceptionV3.setText(QCoreApplication.translate("frameless_dialog", u"\"InceptionV3\": 0.898", None))
        self.EfficientNetB4.setText(QCoreApplication.translate("frameless_dialog", u"\"EfficientNetB4\": 0.947", None))
        self.VGG19.setText(QCoreApplication.translate("frameless_dialog", u"\"VGG19\": 0.707", None))
        self.radioButton.setText(QCoreApplication.translate("frameless_dialog", u"\u5168\u9009", None))
    # retranslateUi

