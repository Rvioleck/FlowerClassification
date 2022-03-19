# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(554, 400)
        AboutWindow.setMinimumSize(QSize(554, 400))
        AboutWindow.setMaximumSize(QSize(554, 400))
        icon = QIcon()
        icon.addFile(u"images/\u82b1\u6735.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(AboutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color:rgb(235, 255, 244)\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 151, 284))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        font.setBold(False)
        self.layoutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 28))
        self.label_11.setMaximumSize(QSize(50, 28))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 28))
        self.label_10.setMaximumSize(QSize(30, 28))
        self.label_10.setFont(font)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 28))
        self.label_12.setMaximumSize(QSize(30, 28))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color: rgb(222, 60, 60)")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_12)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 28))
        self.label.setMaximumSize(QSize(50, 28))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 28))
        self.label_2.setMaximumSize(QSize(30, 28))
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 28))
        self.label_3.setMaximumSize(QSize(30, 28))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 148, 217)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 28))
        self.label_7.setMaximumSize(QSize(50, 28))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 28))
        self.label_8.setMaximumSize(QSize(30, 28))
        self.label_8.setFont(font)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 28))
        self.label_9.setMaximumSize(QSize(30, 28))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(218, 187, 171)")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 28))
        self.label_19.setMaximumSize(QSize(50, 28))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 28))
        self.label_20.setMaximumSize(QSize(30, 28))
        self.label_20.setFont(font)
        self.label_20.setPixmap(QPixmap(u"images/flowers/daisy.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_20)

        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 28))
        self.label_21.setMaximumSize(QSize(30, 28))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background-color:rgb(241, 203, 6)")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_21)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 28))
        self.label_22.setMaximumSize(QSize(50, 28))
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_22)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 28))
        self.label_23.setMaximumSize(QSize(30, 28))
        self.label_23.setFont(font)
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_23)

        self.label_24 = QLabel(self.layoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 28))
        self.label_24.setMaximumSize(QSize(30, 28))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"background-color:rgb(96, 67, 1)")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_24)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_28 = QLabel(self.layoutWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 28))
        self.label_28.setMaximumSize(QSize(50, 28))
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_28)

        self.label_29 = QLabel(self.layoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 28))
        self.label_29.setMaximumSize(QSize(30, 28))
        self.label_29.setFont(font)
        self.label_29.setPixmap(QPixmap(u"images/flowers/gardenia.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_29)

        self.label_30 = QLabel(self.layoutWidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 28))
        self.label_30.setMaximumSize(QSize(30, 28))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"background-color:rgb(187, 187, 187)")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_30)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 28))
        self.label_4.setMaximumSize(QSize(50, 28))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 28))
        self.label_5.setMaximumSize(QSize(30, 28))
        self.label_5.setFont(font)
        self.label_5.setPixmap(QPixmap(u"images/flowers/hibiscus.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 28))
        self.label_6.setMaximumSize(QSize(30, 28))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color:rgb(227, 58, 91)")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 28))
        self.label_14.setMaximumSize(QSize(50, 28))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 28))
        self.label_15.setMaximumSize(QSize(30, 28))
        self.label_15.setFont(font)
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 28))
        self.label_16.setMaximumSize(QSize(30, 28))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"background-color:rgb(245,156,185)")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_16)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.layoutWidget_4 = QWidget(self.centralwidget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(200, 60, 151, 284))
        self.layoutWidget_4.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_25 = QLabel(self.layoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 28))
        self.label_25.setMaximumSize(QSize(50, 28))
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_25)

        self.label_26 = QLabel(self.layoutWidget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 28))
        self.label_26.setMaximumSize(QSize(30, 28))
        self.label_26.setFont(font)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_26)

        self.label_27 = QLabel(self.layoutWidget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 28))
        self.label_27.setMaximumSize(QSize(30, 28))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"background-color:rgb(169, 177, 232)")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_27)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_31 = QLabel(self.layoutWidget_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(50, 28))
        self.label_31.setMaximumSize(QSize(50, 28))
        self.label_31.setFont(font)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_31)

        self.label_32 = QLabel(self.layoutWidget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 28))
        self.label_32.setMaximumSize(QSize(30, 28))
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_32)

        self.label_33 = QLabel(self.layoutWidget_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 28))
        self.label_33.setMaximumSize(QSize(30, 28))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"background-color:rgb(153, 69, 253)")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_33)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_34 = QLabel(self.layoutWidget_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(50, 28))
        self.label_34.setMaximumSize(QSize(50, 28))
        self.label_34.setFont(font)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_34)

        self.label_35 = QLabel(self.layoutWidget_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 28))
        self.label_35.setMaximumSize(QSize(30, 28))
        self.label_35.setFont(font)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_35)

        self.label_36 = QLabel(self.layoutWidget_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 28))
        self.label_36.setMaximumSize(QSize(30, 28))
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"background-color:rgb(216, 158, 221)")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_36)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_37 = QLabel(self.layoutWidget_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 28))
        self.label_37.setMaximumSize(QSize(50, 28))
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_37)

        self.label_38 = QLabel(self.layoutWidget_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 28))
        self.label_38.setMaximumSize(QSize(30, 28))
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_38)

        self.label_39 = QLabel(self.layoutWidget_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 28))
        self.label_39.setMaximumSize(QSize(30, 28))
        self.label_39.setFont(font)
        self.label_39.setStyleSheet(u"background-color:rgb(176, 197, 122)")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_39)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_40 = QLabel(self.layoutWidget_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 28))
        self.label_40.setMaximumSize(QSize(50, 28))
        self.label_40.setFont(font)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_40)

        self.label_41 = QLabel(self.layoutWidget_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 28))
        self.label_41.setMaximumSize(QSize(30, 28))
        self.label_41.setFont(font)
        self.label_41.setPixmap(QPixmap(u"images/flowers/lotus.png"))
        self.label_41.setScaledContents(True)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_41)

        self.label_42 = QLabel(self.layoutWidget_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 28))
        self.label_42.setMaximumSize(QSize(30, 28))
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(u"background-color:rgb(106, 135, 89)")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_42)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_43 = QLabel(self.layoutWidget_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(50, 28))
        self.label_43.setMaximumSize(QSize(50, 28))
        self.label_43.setFont(font)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_43)

        self.label_44 = QLabel(self.layoutWidget_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 28))
        self.label_44.setMaximumSize(QSize(30, 28))
        self.label_44.setFont(font)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_44)

        self.label_45 = QLabel(self.layoutWidget_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 28))
        self.label_45.setMaximumSize(QSize(30, 28))
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"background-color:rgb(28, 77, 183)")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_45)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_46 = QLabel(self.layoutWidget_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(50, 28))
        self.label_46.setMaximumSize(QSize(50, 28))
        self.label_46.setFont(font)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_46)

        self.label_47 = QLabel(self.layoutWidget_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 28))
        self.label_47.setMaximumSize(QSize(30, 28))
        self.label_47.setFont(font)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_47)

        self.label_48 = QLabel(self.layoutWidget_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 28))
        self.label_48.setMaximumSize(QSize(30, 28))
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"background-color:rgb(249, 245, 138)")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_48)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(self.layoutWidget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 28))
        self.label_17.setMaximumSize(QSize(50, 28))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.label_18 = QLabel(self.layoutWidget_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 28))
        self.label_18.setMaximumSize(QSize(30, 28))
        self.label_18.setFont(font)
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_18)

        self.label_71 = QLabel(self.layoutWidget_4)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 28))
        self.label_71.setMaximumSize(QSize(30, 28))
        self.label_71.setFont(font)
        self.label_71.setStyleSheet(u"background-color:rgb(236, 181, 1)")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_71)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.layoutWidget_6 = QWidget(self.centralwidget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(380, 60, 151, 284))
        self.layoutWidget_6.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_49 = QLabel(self.layoutWidget_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(50, 28))
        self.label_49.setMaximumSize(QSize(50, 28))
        self.label_49.setFont(font)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_49)

        self.label_50 = QLabel(self.layoutWidget_6)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(30, 28))
        self.label_50.setMaximumSize(QSize(30, 28))
        self.label_50.setFont(font)
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_50)

        self.label_51 = QLabel(self.layoutWidget_6)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(30, 28))
        self.label_51.setMaximumSize(QSize(30, 28))
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"background-color:rgb(224, 189, 213)")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_51)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_52 = QLabel(self.layoutWidget_6)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(50, 28))
        self.label_52.setMaximumSize(QSize(50, 28))
        self.label_52.setFont(font)
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_52)

        self.label_53 = QLabel(self.layoutWidget_6)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(30, 28))
        self.label_53.setMaximumSize(QSize(30, 28))
        self.label_53.setFont(font)
        self.label_53.setPixmap(QPixmap(u"images/flowers/peony.png"))
        self.label_53.setScaledContents(True)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_53)

        self.label_54 = QLabel(self.layoutWidget_6)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(30, 28))
        self.label_54.setMaximumSize(QSize(30, 28))
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"background-color:rgb(189, 115, 121)")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_54)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_55 = QLabel(self.layoutWidget_6)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(50, 28))
        self.label_55.setMaximumSize(QSize(50, 28))
        self.label_55.setFont(font)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_55)

        self.label_56 = QLabel(self.layoutWidget_6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(30, 28))
        self.label_56.setMaximumSize(QSize(30, 28))
        self.label_56.setFont(font)
        self.label_56.setScaledContents(True)
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_56)

        self.label_57 = QLabel(self.layoutWidget_6)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(30, 28))
        self.label_57.setMaximumSize(QSize(30, 28))
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"background-color:rgb(185, 73, 79)")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_57)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_58 = QLabel(self.layoutWidget_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(50, 28))
        self.label_58.setMaximumSize(QSize(50, 28))
        self.label_58.setFont(font)
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_58)

        self.label_59 = QLabel(self.layoutWidget_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(30, 28))
        self.label_59.setMaximumSize(QSize(30, 28))
        self.label_59.setFont(font)
        self.label_59.setScaledContents(True)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_59)

        self.label_60 = QLabel(self.layoutWidget_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(30, 28))
        self.label_60.setMaximumSize(QSize(30, 28))
        self.label_60.setFont(font)
        self.label_60.setStyleSheet(u"background-color:rgb(120, 0, 20)")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_60)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_61 = QLabel(self.layoutWidget_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(50, 28))
        self.label_61.setMaximumSize(QSize(50, 28))
        self.label_61.setFont(font)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_61)

        self.label_62 = QLabel(self.layoutWidget_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(30, 28))
        self.label_62.setMaximumSize(QSize(30, 28))
        self.label_62.setFont(font)
        self.label_62.setScaledContents(True)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_62)

        self.label_63 = QLabel(self.layoutWidget_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(30, 28))
        self.label_63.setMaximumSize(QSize(30, 28))
        self.label_63.setFont(font)
        self.label_63.setStyleSheet(u"background-color:rgb(181, 97, 127)")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_63)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_64 = QLabel(self.layoutWidget_6)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(50, 28))
        self.label_64.setMaximumSize(QSize(50, 28))
        self.label_64.setFont(font)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_64)

        self.label_65 = QLabel(self.layoutWidget_6)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(30, 28))
        self.label_65.setMaximumSize(QSize(30, 28))
        self.label_65.setFont(font)
        self.label_65.setPixmap(QPixmap(u"images/flowers/sunflower.png"))
        self.label_65.setScaledContents(True)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_65)

        self.label_66 = QLabel(self.layoutWidget_6)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(30, 28))
        self.label_66.setMaximumSize(QSize(30, 28))
        self.label_66.setFont(font)
        self.label_66.setStyleSheet(u"background-color:rgb(205, 134, 18)")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_66)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_67 = QLabel(self.layoutWidget_6)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(50, 28))
        self.label_67.setMaximumSize(QSize(50, 28))
        self.label_67.setFont(font)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_67)

        self.label_68 = QLabel(self.layoutWidget_6)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(30, 28))
        self.label_68.setMaximumSize(QSize(30, 28))
        self.label_68.setFont(font)
        self.label_68.setScaledContents(True)
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_68)

        self.label_69 = QLabel(self.layoutWidget_6)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(30, 28))
        self.label_69.setMaximumSize(QSize(30, 28))
        self.label_69.setFont(font)
        self.label_69.setStyleSheet(u"background-color:rgb(240, 96, 140)")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_69)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_72 = QLabel(self.layoutWidget_6)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(50, 28))
        self.label_72.setMaximumSize(QSize(50, 28))
        self.label_72.setFont(font)
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_72)

        self.label_73 = QLabel(self.layoutWidget_6)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(0, 28))
        self.label_73.setMaximumSize(QSize(30, 28))
        self.label_73.setFont(font)
        self.label_73.setScaledContents(True)
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_73)

        self.label_74 = QLabel(self.layoutWidget_6)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 28))
        self.label_74.setMaximumSize(QSize(30, 28))
        self.label_74.setFont(font)
        self.label_74.setStyleSheet(u"background-color:rgb(229, 223, 105)")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_74)


        self.verticalLayout_3.addLayout(self.horizontalLayout_25)

        self.label_70 = QLabel(self.centralwidget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(90, 20, 371, 31))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_70.setFont(font1)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(21, 359, 471, 31))
        self.label_13.setOpenExternalLinks(True)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(504, 357, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"images/\u4f7f\u7528\u8bf4\u660e.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(32, 32))
        self.toolButton.setAutoRaise(True)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"\u5173\u4e8e\u672c\u8f6f\u4ef6", None))
#if QT_CONFIG(tooltip)
        AboutWindow.setToolTip(QCoreApplication.translate("AboutWindow", u"\u53f3\u952e\u5173\u95ed\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("AboutWindow", u"\u675c\u9e43\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(222, 60, 60)", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("AboutWindow", u"\u53f6\u5b50\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(255, 148, 217)", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("AboutWindow", u"\u5eb7\u4e43\u99a8", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(218, 187, 171)", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("AboutWindow", u"\u96cf  \u83ca", None))
        self.label_20.setText("")
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(241, 203, 6)", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("AboutWindow", u"\u84b2\u516c\u82f1", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(96, 67, 1)", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("AboutWindow", u"\u6800\u5b50\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(187, 187, 187)", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("AboutWindow", u"\u6728\u69ff\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(227, 58, 91)", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("AboutWindow", u"\u5c71\u8336\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(227, 58, 91)", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("AboutWindow", u"\u7ee3\u7403\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(169, 177, 232)", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("AboutWindow", u"\u9e22\u5c3e\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(153, 69, 253)", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("AboutWindow", u"\u4e01\u9999\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(216, 158, 221)", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("AboutWindow", u"\u767e\u5408\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_39.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(176, 197, 122)", None))
#endif // QT_CONFIG(tooltip)
        self.label_40.setText(QCoreApplication.translate("AboutWindow", u"\u8377  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_42.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(106, 135, 89)", None))
#endif // QT_CONFIG(tooltip)
        self.label_43.setText(QCoreApplication.translate("AboutWindow", u"\u7275\u725b\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_45.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(28, 77, 183)", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("AboutWindow", u"\u6c34\u4ed9\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_48.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(249, 245, 138)", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("AboutWindow", u"\u83ca  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_71.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(227, 58, 91)", None))
#endif // QT_CONFIG(tooltip)
        self.label_49.setText(QCoreApplication.translate("AboutWindow", u"\u6843  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_51.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(224, 189, 213)", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("AboutWindow", u"\u7261\u4e39\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_54.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(189, 115, 121)", None))
#endif // QT_CONFIG(tooltip)
        self.label_55.setText(QCoreApplication.translate("AboutWindow", u"\u8774\u8776\u5170", None))
#if QT_CONFIG(tooltip)
        self.label_57.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(185, 73, 79)", None))
#endif // QT_CONFIG(tooltip)
        self.label_58.setText(QCoreApplication.translate("AboutWindow", u"\u73ab\u7470\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_60.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(120, 0, 20)", None))
#endif // QT_CONFIG(tooltip)
        self.label_61.setText(QCoreApplication.translate("AboutWindow", u"\u6a31  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_63.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(181, 97, 127)", None))
#endif // QT_CONFIG(tooltip)
        self.label_64.setText(QCoreApplication.translate("AboutWindow", u"\u5411\u65e5\u8475", None))
#if QT_CONFIG(tooltip)
        self.label_66.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(205, 134, 18)", None))
#endif // QT_CONFIG(tooltip)
        self.label_67.setText(QCoreApplication.translate("AboutWindow", u"\u90c1\u91d1\u9999", None))
#if QT_CONFIG(tooltip)
        self.label_69.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(240, 96, 140)", None))
#endif // QT_CONFIG(tooltip)
        self.label_72.setText(QCoreApplication.translate("AboutWindow", u"\u6842  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_74.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(227, 58, 91)", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("AboutWindow", u"\u672c\u8f6f\u4ef6\u53ef\u4ee5\u8fdb\u884c\u4ee5\u4e0b24\u7c7b\u82b1\u6735\u56fe\u50cf\u5206\u7c7b", None))
        self.label_13.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u672c\u9879\u76ee\u5b8c\u5168\u5f00\u6e90\uff0c\u9879\u76ee\u5e93\u5730\u5740\uff1a</span><a href=\"https://github.com/Rvioleck/FlowerClassification\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Rvioleck/FlowerClassification</span></a></p></body></html>", None))
        self.toolButton.setText(QCoreApplication.translate("AboutWindow", u"...", None))
    # retranslateUi

