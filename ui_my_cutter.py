# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_cutter.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QDialog, QGraphicsView,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1100, 786)
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 1101, 691))
        self.cutPushButton = QPushButton(Dialog)
        self.cutPushButton.setObjectName(u"cutPushButton")
        self.cutPushButton.setGeometry(QRect(910, 720, 41, 41))
        self.cutPushButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.cutPushButton.setIconSize(QSize(32, 32))
        self.cutPushButton.setCheckable(True)
        self.cutPushButton.setFlat(True)
        self.savePushButton = QPushButton(Dialog)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(990, 720, 91, 40))
        self.rightRotateToolButton = QToolButton(Dialog)
        self.rightRotateToolButton.setObjectName(u"rightRotateToolButton")
        self.rightRotateToolButton.setGeometry(QRect(43, 710, 71, 61))
        self.rightRotateToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"images/\u53f3\u65cb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightRotateToolButton.setIcon(icon)
        self.rightRotateToolButton.setIconSize(QSize(36, 36))
        self.rightRotateToolButton.setCheckable(False)
        self.rightRotateToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.rightRotateToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.rightRotateToolButton.setAutoRaise(True)
        self.leftRotateToolButton = QToolButton(Dialog)
        self.leftRotateToolButton.setObjectName(u"leftRotateToolButton")
        self.leftRotateToolButton.setGeometry(QRect(173, 710, 71, 61))
        self.leftRotateToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/\u5de6\u65cb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftRotateToolButton.setIcon(icon1)
        self.leftRotateToolButton.setIconSize(QSize(36, 36))
        self.leftRotateToolButton.setCheckable(False)
        self.leftRotateToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.leftRotateToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.leftRotateToolButton.setAutoRaise(True)
        self.horizontalFlipToolButton = QToolButton(Dialog)
        self.horizontalFlipToolButton.setObjectName(u"horizontalFlipToolButton")
        self.horizontalFlipToolButton.setGeometry(QRect(336, 710, 71, 61))
        self.horizontalFlipToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"images/\u6c34\u5e73\u7ffb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.horizontalFlipToolButton.setIcon(icon2)
        self.horizontalFlipToolButton.setIconSize(QSize(36, 36))
        self.horizontalFlipToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.horizontalFlipToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.horizontalFlipToolButton.setAutoRaise(True)
        self.verticalFlipToolButton = QToolButton(Dialog)
        self.verticalFlipToolButton.setObjectName(u"verticalFlipToolButton")
        self.verticalFlipToolButton.setGeometry(QRect(261, 710, 71, 61))
        self.verticalFlipToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"images/\u5782\u76f4\u7ffb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verticalFlipToolButton.setIcon(icon3)
        self.verticalFlipToolButton.setIconSize(QSize(36, 36))
        self.verticalFlipToolButton.setCheckable(False)
        self.verticalFlipToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.verticalFlipToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.verticalFlipToolButton.setAutoRaise(True)
        self.rotationDial = QDial(Dialog)
        self.rotationDial.setObjectName(u"rotationDial")
        self.rotationDial.setGeometry(QRect(118, 710, 50, 50))
        self.rotationDial.setMaximum(360)
        self.rotationDial.setSingleStep(5)
        self.rotationDial.setPageStep(20)
        self.rotationDial.setInvertedAppearance(False)
        self.rotationDial.setInvertedControls(False)
        self.rotationDial.setWrapping(True)
        self.rotationDial.setNotchesVisible(True)
        self.horizontalSliderBrightness = QSlider(Dialog)
        self.horizontalSliderBrightness.setObjectName(u"horizontalSliderBrightness")
        self.horizontalSliderBrightness.setGeometry(QRect(485, 709, 160, 22))
        self.horizontalSliderBrightness.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSliderBrightness.setMinimum(-100)
        self.horizontalSliderBrightness.setMaximum(100)
        self.horizontalSliderBrightness.setOrientation(Qt.Horizontal)
        self.horizontalSliderContrast = QSlider(Dialog)
        self.horizontalSliderContrast.setObjectName(u"horizontalSliderContrast")
        self.horizontalSliderContrast.setGeometry(QRect(485, 750, 160, 22))
        self.horizontalSliderContrast.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSliderContrast.setMinimum(-5)
        self.horizontalSliderContrast.setMaximum(5)
        self.horizontalSliderContrast.setPageStep(2)
        self.horizontalSliderContrast.setOrientation(Qt.Horizontal)
        self.brightness_label = QLabel(Dialog)
        self.brightness_label.setObjectName(u"brightness_label")
        self.brightness_label.setGeometry(QRect(445, 705, 31, 31))
        self.brightness_label.setPixmap(QPixmap(u"images/\u4eae\u5ea6.png"))
        self.brightness_label.setScaledContents(True)
        self.contrast_label = QLabel(Dialog)
        self.contrast_label.setObjectName(u"contrast_label")
        self.contrast_label.setGeometry(QRect(450, 749, 21, 21))
        self.contrast_label.setPixmap(QPixmap(u"images/\u5bf9\u6bd4\u5ea6.png"))
        self.contrast_label.setScaledContents(True)
        self.horizontalSliderHues = QSlider(Dialog)
        self.horizontalSliderHues.setObjectName(u"horizontalSliderHues")
        self.horizontalSliderHues.setGeometry(QRect(700, 709, 160, 22))
        self.horizontalSliderHues.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSliderHues.setMinimum(0)
        self.horizontalSliderHues.setMaximum(100)
        self.horizontalSliderHues.setOrientation(Qt.Horizontal)
        self.horizontalSliderSaturation = QSlider(Dialog)
        self.horizontalSliderSaturation.setObjectName(u"horizontalSliderSaturation")
        self.horizontalSliderSaturation.setGeometry(QRect(700, 750, 160, 22))
        self.horizontalSliderSaturation.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSliderSaturation.setMinimum(-5)
        self.horizontalSliderSaturation.setMaximum(5)
        self.horizontalSliderSaturation.setPageStep(2)
        self.horizontalSliderSaturation.setOrientation(Qt.Horizontal)
        self.saturation_label = QLabel(Dialog)
        self.saturation_label.setObjectName(u"saturation_label")
        self.saturation_label.setGeometry(QRect(665, 749, 21, 21))
        self.saturation_label.setPixmap(QPixmap(u"images/\u9971\u548c\u5ea6.png"))
        self.saturation_label.setScaledContents(True)
        self.hue_label = QLabel(Dialog)
        self.hue_label.setObjectName(u"hue_label")
        self.hue_label.setGeometry(QRect(666, 709, 21, 21))
        self.hue_label.setPixmap(QPixmap(u"images/\u8272\u76f8.png"))
        self.hue_label.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.cutPushButton.setToolTip(QCoreApplication.translate("Dialog", u"\u88c1\u526a", None))
#endif // QT_CONFIG(tooltip)
        self.savePushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
#if QT_CONFIG(tooltip)
        self.rightRotateToolButton.setToolTip(QCoreApplication.translate("Dialog", u"\u987a\u65f6\u9488\u65cb\u8f6c90\u00b0", None))
#endif // QT_CONFIG(tooltip)
        self.rightRotateToolButton.setText(QCoreApplication.translate("Dialog", u"\u987a\u65f6\u9488\u65cb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.leftRotateToolButton.setToolTip(QCoreApplication.translate("Dialog", u"\u9006\u65f6\u9488\u65cb\u8f6c90\u00b0", None))
#endif // QT_CONFIG(tooltip)
        self.leftRotateToolButton.setText(QCoreApplication.translate("Dialog", u"\u9006\u65f6\u9488\u65cb\u8f6c", None))
        self.horizontalFlipToolButton.setText(QCoreApplication.translate("Dialog", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.verticalFlipToolButton.setText(QCoreApplication.translate("Dialog", u"\u7ad6\u76f4\u7ffb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.rotationDial.setToolTip(QCoreApplication.translate("Dialog", u"\u653e\u5927\u5668", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.horizontalSliderBrightness.setToolTip(QCoreApplication.translate("Dialog", u"\u4eae\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.horizontalSliderContrast.setToolTip(QCoreApplication.translate("Dialog", u"\u5bf9\u6bd4\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.brightness_label.setToolTip(QCoreApplication.translate("Dialog", u"\u4eae\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.brightness_label.setText("")
#if QT_CONFIG(tooltip)
        self.contrast_label.setToolTip(QCoreApplication.translate("Dialog", u"\u5bf9\u6bd4\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.contrast_label.setText("")
#if QT_CONFIG(tooltip)
        self.horizontalSliderHues.setToolTip(QCoreApplication.translate("Dialog", u"\u8272\u76f8", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.horizontalSliderSaturation.setToolTip(QCoreApplication.translate("Dialog", u"\u5bf9\u6bd4\u5ea6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.saturation_label.setToolTip(QCoreApplication.translate("Dialog", u"\u5bf9\u6bd4\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.saturation_label.setText("")
#if QT_CONFIG(tooltip)
        self.hue_label.setToolTip(QCoreApplication.translate("Dialog", u"\u8272\u76f8", None))
#endif // QT_CONFIG(tooltip)
        self.hue_label.setText("")
    # retranslateUi

