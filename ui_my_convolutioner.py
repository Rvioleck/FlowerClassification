# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_convolutioner.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(827, 428)
        self.orginImage = QLabel(Dialog)
        self.orginImage.setObjectName(u"orginImage")
        self.orginImage.setGeometry(QRect(30, 70, 224, 224))
        self.orginImage.setFrameShape(QFrame.WinPanel)
        self.orginImage.setFrameShadow(QFrame.Plain)
        self.orginImage.setScaledContents(True)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(493, 166, 41, 31))
        icon = QIcon()
        icon.addFile(u"images/\u53f3\u7bad\u5934.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setFlat(True)
        self.convolutionImage = QLabel(Dialog)
        self.convolutionImage.setObjectName(u"convolutionImage")
        self.convolutionImage.setGeometry(QRect(550, 70, 224, 224))
        self.convolutionImage.setFrameShape(QFrame.WinPanel)
        self.convolutionImage.setFrameShadow(QFrame.Plain)
        self.convolutionImage.setScaledContents(True)
        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(640, 310, 75, 24))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(440, 320, 111, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(259, 70, 91, 221))
        self.label.setPixmap(QPixmap(u"images/\u80cc\u666f.png"))
        self.label.setScaledContents(True)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 320, 371, 81))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_button = QPushButton(self.widget)
        self.slide_button.setObjectName(u"slide_button")

        self.gridLayout_2.addWidget(self.slide_button, 0, 0, 1, 1)

        self.horizonal_button = QPushButton(self.widget)
        self.horizonal_button.setObjectName(u"horizonal_button")

        self.gridLayout_2.addWidget(self.horizonal_button, 0, 1, 1, 1)

        self.sharp_button = QPushButton(self.widget)
        self.sharp_button.setObjectName(u"sharp_button")

        self.gridLayout_2.addWidget(self.sharp_button, 0, 2, 1, 1)

        self.gaosi_slide_button = QPushButton(self.widget)
        self.gaosi_slide_button.setObjectName(u"gaosi_slide_button")

        self.gridLayout_2.addWidget(self.gaosi_slide_button, 1, 0, 1, 1)

        self.vertical_button = QPushButton(self.widget)
        self.vertical_button.setObjectName(u"vertical_button")

        self.gridLayout_2.addWidget(self.vertical_button, 1, 1, 1, 1)

        self.ex_sharp_button = QPushButton(self.widget)
        self.ex_sharp_button.setObjectName(u"ex_sharp_button")

        self.gridLayout_2.addWidget(self.ex_sharp_button, 1, 2, 1, 1)

        self.textEdit_3 = QTextEdit(Dialog)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(434, 114, 45, 45))
        self.textEdit_3.setMinimumSize(QSize(45, 45))
        self.textEdit_3.setMaximumSize(QSize(45, 45))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_3.setFrameShape(QFrame.Box)
        self.textEdit_3.setFrameShadow(QFrame.Plain)
        self.textEdit_3.setLineWidth(2)
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7 = QTextEdit(Dialog)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(342, 206, 45, 45))
        self.textEdit_7.setMinimumSize(QSize(45, 45))
        self.textEdit_7.setMaximumSize(QSize(45, 45))
        self.textEdit_7.setFont(font)
        self.textEdit_7.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_7.setFrameShape(QFrame.Box)
        self.textEdit_7.setFrameShadow(QFrame.Plain)
        self.textEdit_7.setLineWidth(2)
        self.textEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9 = QTextEdit(Dialog)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(434, 206, 45, 45))
        self.textEdit_9.setMinimumSize(QSize(45, 45))
        self.textEdit_9.setMaximumSize(QSize(45, 45))
        self.textEdit_9.setFont(font)
        self.textEdit_9.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_9.setFrameShape(QFrame.Box)
        self.textEdit_9.setFrameShadow(QFrame.Plain)
        self.textEdit_9.setLineWidth(2)
        self.textEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_1 = QTextEdit(Dialog)
        self.textEdit_1.setObjectName(u"textEdit_1")
        self.textEdit_1.setGeometry(QRect(342, 114, 45, 45))
        self.textEdit_1.setMinimumSize(QSize(45, 45))
        self.textEdit_1.setMaximumSize(QSize(45, 45))
        self.textEdit_1.setFont(font)
        self.textEdit_1.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_1.setFrameShape(QFrame.Box)
        self.textEdit_1.setFrameShadow(QFrame.Plain)
        self.textEdit_1.setLineWidth(2)
        self.textEdit_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4 = QTextEdit(Dialog)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(342, 160, 45, 45))
        self.textEdit_4.setMinimumSize(QSize(45, 45))
        self.textEdit_4.setMaximumSize(QSize(45, 45))
        self.textEdit_4.setFont(font)
        self.textEdit_4.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_4.setFrameShape(QFrame.Box)
        self.textEdit_4.setFrameShadow(QFrame.Plain)
        self.textEdit_4.setLineWidth(2)
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_8 = QTextEdit(Dialog)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(388, 206, 45, 45))
        self.textEdit_8.setMinimumSize(QSize(45, 45))
        self.textEdit_8.setMaximumSize(QSize(45, 45))
        self.textEdit_8.setFont(font)
        self.textEdit_8.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_8.setFrameShape(QFrame.Box)
        self.textEdit_8.setFrameShadow(QFrame.Plain)
        self.textEdit_8.setLineWidth(2)
        self.textEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6 = QTextEdit(Dialog)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(434, 160, 45, 45))
        self.textEdit_6.setMinimumSize(QSize(45, 45))
        self.textEdit_6.setMaximumSize(QSize(45, 45))
        self.textEdit_6.setFont(font)
        self.textEdit_6.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_6.setFrameShape(QFrame.Box)
        self.textEdit_6.setFrameShadow(QFrame.Plain)
        self.textEdit_6.setLineWidth(2)
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(388, 114, 45, 45))
        self.textEdit_2.setMinimumSize(QSize(45, 45))
        self.textEdit_2.setMaximumSize(QSize(45, 45))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_2.setFrameShape(QFrame.Box)
        self.textEdit_2.setFrameShadow(QFrame.Plain)
        self.textEdit_2.setLineWidth(2)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5 = QTextEdit(Dialog)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(388, 160, 45, 45))
        self.textEdit_5.setMinimumSize(QSize(45, 45))
        self.textEdit_5.setMaximumSize(QSize(45, 45))
        self.textEdit_5.setFont(font)
        self.textEdit_5.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_5.setFrameShape(QFrame.Box)
        self.textEdit_5.setFrameShadow(QFrame.Plain)
        self.textEdit_5.setLineWidth(2)
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        QWidget.setTabOrder(self.textEdit_1, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.textEdit_3)
        QWidget.setTabOrder(self.textEdit_3, self.textEdit_4)
        QWidget.setTabOrder(self.textEdit_4, self.textEdit_5)
        QWidget.setTabOrder(self.textEdit_5, self.textEdit_6)
        QWidget.setTabOrder(self.textEdit_6, self.textEdit_7)
        QWidget.setTabOrder(self.textEdit_7, self.textEdit_8)
        QWidget.setTabOrder(self.textEdit_8, self.textEdit_9)
        QWidget.setTabOrder(self.textEdit_9, self.slide_button)
        QWidget.setTabOrder(self.slide_button, self.gaosi_slide_button)
        QWidget.setTabOrder(self.gaosi_slide_button, self.horizonal_button)
        QWidget.setTabOrder(self.horizonal_button, self.vertical_button)
        QWidget.setTabOrder(self.vertical_button, self.sharp_button)
        QWidget.setTabOrder(self.sharp_button, self.pushButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.orginImage.setText("")
        self.pushButton.setText("")
        self.convolutionImage.setText("")
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.label.setText("")
        self.slide_button.setText(QCoreApplication.translate("Dialog", u"\u5e73\u6ed1\u5377\u79ef\u6838", None))
        self.horizonal_button.setText(QCoreApplication.translate("Dialog", u"\u6c34\u5e73\u68af\u5ea6\u5377\u79ef\u6838", None))
        self.sharp_button.setText(QCoreApplication.translate("Dialog", u"\u9510\u5316\u5377\u79ef\u6838", None))
        self.gaosi_slide_button.setText(QCoreApplication.translate("Dialog", u"\u9ad8\u65af\u5e73\u6ed1\u5377\u79ef\u6838", None))
        self.vertical_button.setText(QCoreApplication.translate("Dialog", u"\u5782\u76f4\u68af\u5ea6\u5377\u79ef\u6838", None))
        self.ex_sharp_button.setText(QCoreApplication.translate("Dialog", u"\u5f3a\u5316\u9510\u5316\u5377\u79ef\u6838", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_1.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>", None))
    # retranslateUi

