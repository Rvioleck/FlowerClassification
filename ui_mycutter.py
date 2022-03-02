# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mycutter.ui'
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
                               QPushButton, QSizePolicy, QToolButton, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1022, 768)
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 1021, 691))
        self.putButton_cut = QPushButton(Dialog)
        self.putButton_cut.setObjectName(u"putButton_cut")
        self.putButton_cut.setGeometry(QRect(740, 710, 91, 31))
        self.putButton_cut.setStyleSheet(u"QPushButton\n"
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
        self.putButton_cut.setCheckable(True)
        self.putButton_save = QPushButton(Dialog)
        self.putButton_save.setObjectName(u"putButton_save")
        self.putButton_save.setEnabled(False)
        self.putButton_save.setGeometry(QRect(880, 710, 91, 31))
        self.putButton_save.setStyleSheet(u"QPushButton\n"
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
        self.rightRotateToolButton = QToolButton(Dialog)
        self.rightRotateToolButton.setObjectName(u"rightRotateToolButton")
        self.rightRotateToolButton.setGeometry(QRect(50, 700, 71, 61))
        icon = QIcon()
        icon.addFile(u"images/\u987a\u65f6\u9488.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightRotateToolButton.setIcon(icon)
        self.rightRotateToolButton.setIconSize(QSize(36, 36))
        self.rightRotateToolButton.setCheckable(False)
        self.rightRotateToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.rightRotateToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.rightRotateToolButton.setAutoRaise(True)
        self.leftRotateToolButton = QToolButton(Dialog)
        self.leftRotateToolButton.setObjectName(u"leftRotateToolButton")
        self.leftRotateToolButton.setGeometry(QRect(180, 700, 71, 61))
        icon1 = QIcon()
        icon1.addFile(u"images/\u9006\u65f6\u9488.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftRotateToolButton.setIcon(icon1)
        self.leftRotateToolButton.setIconSize(QSize(36, 36))
        self.leftRotateToolButton.setCheckable(False)
        self.leftRotateToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.leftRotateToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.leftRotateToolButton.setAutoRaise(True)
        self.horizontalFlipToolButton = QToolButton(Dialog)
        self.horizontalFlipToolButton.setObjectName(u"horizontalFlipToolButton")
        self.horizontalFlipToolButton.setGeometry(QRect(400, 700, 71, 61))
        icon2 = QIcon()
        icon2.addFile(u"images/\u6c34\u5e73\u7ffb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.horizontalFlipToolButton.setIcon(icon2)
        self.horizontalFlipToolButton.setIconSize(QSize(36, 36))
        self.horizontalFlipToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.horizontalFlipToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.horizontalFlipToolButton.setAutoRaise(True)
        self.verticalFlipToolButton = QToolButton(Dialog)
        self.verticalFlipToolButton.setObjectName(u"verticalFlipToolButton")
        self.verticalFlipToolButton.setGeometry(QRect(310, 700, 71, 61))
        icon3 = QIcon()
        icon3.addFile(u"images/\u7ad6\u76f4\u7ffb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verticalFlipToolButton.setIcon(icon3)
        self.verticalFlipToolButton.setIconSize(QSize(36, 36))
        self.verticalFlipToolButton.setCheckable(False)
        self.verticalFlipToolButton.setPopupMode(QToolButton.DelayedPopup)
        self.verticalFlipToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.verticalFlipToolButton.setAutoRaise(True)
        self.rotationDial = QDial(Dialog)
        self.rotationDial.setObjectName(u"rotationDial")
        self.rotationDial.setGeometry(QRect(125, 700, 50, 50))
        self.rotationDial.setMaximum(360)
        self.rotationDial.setSingleStep(5)
        self.rotationDial.setPageStep(20)
        self.rotationDial.setInvertedAppearance(False)
        self.rotationDial.setInvertedControls(False)
        self.rotationDial.setWrapping(True)
        self.rotationDial.setNotchesVisible(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.putButton_cut.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u88c1\u526a", None))
        self.putButton_save.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.rightRotateToolButton.setText(
            QCoreApplication.translate("Dialog", u"\u987a\u65f6\u9488\u65cb\u8f6c", None))
        self.leftRotateToolButton.setText(QCoreApplication.translate("Dialog", u"\u9006\u65f6\u9488\u65cb\u8f6c", None))
        self.horizontalFlipToolButton.setText(QCoreApplication.translate("Dialog", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.verticalFlipToolButton.setText(QCoreApplication.translate("Dialog", u"\u7ad6\u76f4\u7ffb\u8f6c", None))
    # retranslateUi
