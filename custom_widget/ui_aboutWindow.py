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
import custom_widget.flowers_rc

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(600, 600)
        AboutWindow.setMinimumSize(QSize(600, 600))
        AboutWindow.setMaximumSize(QSize(600, 600))
        icon = QIcon()
        icon.addFile(u"images/\u82b1\u6735.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(AboutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color:rgb(235, 255, 244)\n"
"}")
        self.label_70 = QLabel(self.centralwidget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(120, 30, 371, 31))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_70.setFont(font)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(37, 532, 471, 31))
        self.label_13.setOpenExternalLinks(True)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(530, 530, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"images/\u4f7f\u7528\u8bf4\u660e.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(32, 32))
        self.toolButton.setAutoRaise(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 83, 531, 431))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_75 = QLabel(self.layoutWidget)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(50, 28))
        self.label_75.setMaximumSize(QSize(50, 28))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_75.setFont(font1)
        self.label_75.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_75)

        self.label_76 = QLabel(self.layoutWidget)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(50, 15))
        self.label_76.setMaximumSize(QSize(50, 15))
        self.label_76.setFont(font1)
        self.label_76.setStyleSheet(u"background-color: rgb(222, 60, 60)")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_76)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.azalea = QLabel(self.layoutWidget)
        self.azalea.setObjectName(u"azalea")
        self.azalea.setMinimumSize(QSize(60, 60))
        self.azalea.setMaximumSize(QSize(50, 50))
        self.azalea.setFont(font1)
        self.azalea.setPixmap(QPixmap(u"images/flowers/azalea.png"))
        self.azalea.setScaledContents(True)
        self.azalea.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.azalea)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_78 = QLabel(self.layoutWidget)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(50, 28))
        self.label_78.setMaximumSize(QSize(50, 28))
        self.label_78.setFont(font1)
        self.label_78.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_78)

        self.label_79 = QLabel(self.layoutWidget)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(50, 15))
        self.label_79.setMaximumSize(QSize(50, 15))
        self.label_79.setFont(font1)
        self.label_79.setStyleSheet(u"background-color: rgb(255, 148, 217)")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_79)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.label_80 = QLabel(self.layoutWidget)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(60, 60))
        self.label_80.setMaximumSize(QSize(50, 50))
        self.label_80.setFont(font1)
        self.label_80.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_80.setScaledContents(True)
        self.label_80.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_80)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_81 = QLabel(self.layoutWidget)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(50, 28))
        self.label_81.setMaximumSize(QSize(50, 28))
        self.label_81.setFont(font1)
        self.label_81.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_81)

        self.label_82 = QLabel(self.layoutWidget)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(50, 15))
        self.label_82.setMaximumSize(QSize(50, 15))
        self.label_82.setFont(font1)
        self.label_82.setStyleSheet(u"background-color: rgb(245, 156, 185)")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_82)


        self.horizontalLayout_26.addLayout(self.verticalLayout_6)

        self.label_83 = QLabel(self.layoutWidget)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(60, 60))
        self.label_83.setMaximumSize(QSize(50, 50))
        self.label_83.setFont(font1)
        self.label_83.setPixmap(QPixmap(u"images/flowers/camellia.png"))
        self.label_83.setScaledContents(True)
        self.label_83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_83)


        self.verticalLayout.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_84 = QLabel(self.layoutWidget)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(50, 28))
        self.label_84.setMaximumSize(QSize(50, 28))
        self.label_84.setFont(font1)
        self.label_84.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_84)

        self.label_85 = QLabel(self.layoutWidget)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(50, 15))
        self.label_85.setMaximumSize(QSize(50, 15))
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"background-color: rgb(218, 187, 171)")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_85)


        self.horizontalLayout_27.addLayout(self.verticalLayout_7)

        self.label_86 = QLabel(self.layoutWidget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(60, 60))
        self.label_86.setMaximumSize(QSize(50, 50))
        self.label_86.setFont(font1)
        self.label_86.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_86.setScaledContents(True)
        self.label_86.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_86)


        self.verticalLayout.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_90 = QLabel(self.layoutWidget)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(50, 28))
        self.label_90.setMaximumSize(QSize(50, 28))
        self.label_90.setFont(font1)
        self.label_90.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_90)

        self.label_91 = QLabel(self.layoutWidget)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(50, 15))
        self.label_91.setMaximumSize(QSize(50, 15))
        self.label_91.setFont(font1)
        self.label_91.setStyleSheet(u"background-color: rgb(236, 181, 1)")
        self.label_91.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_91)


        self.horizontalLayout_29.addLayout(self.verticalLayout_9)

        self.label_92 = QLabel(self.layoutWidget)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(60, 60))
        self.label_92.setMaximumSize(QSize(50, 50))
        self.label_92.setFont(font1)
        self.label_92.setPixmap(QPixmap(u"images/flowers/chrysanthemum.png"))
        self.label_92.setScaledContents(True)
        self.label_92.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_92)


        self.verticalLayout.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_87 = QLabel(self.layoutWidget)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(50, 28))
        self.label_87.setMaximumSize(QSize(50, 28))
        self.label_87.setFont(font1)
        self.label_87.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_87)

        self.label_88 = QLabel(self.layoutWidget)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(50, 15))
        self.label_88.setMaximumSize(QSize(50, 15))
        self.label_88.setFont(font1)
        self.label_88.setStyleSheet(u"background-color: rgb(241, 203, 6)")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_88)


        self.horizontalLayout_28.addLayout(self.verticalLayout_8)

        self.label_89 = QLabel(self.layoutWidget)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(60, 60))
        self.label_89.setMaximumSize(QSize(50, 50))
        self.label_89.setFont(font1)
        self.label_89.setPixmap(QPixmap(u"images/flowers/daisy.png"))
        self.label_89.setScaledContents(True)
        self.label_89.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_89)


        self.verticalLayout.addLayout(self.horizontalLayout_28)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_93 = QLabel(self.layoutWidget)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(50, 28))
        self.label_93.setMaximumSize(QSize(50, 28))
        self.label_93.setFont(font1)
        self.label_93.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_93)

        self.label_94 = QLabel(self.layoutWidget)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(50, 15))
        self.label_94.setMaximumSize(QSize(50, 15))
        self.label_94.setFont(font1)
        self.label_94.setStyleSheet(u"background-color: rgb(96, 67, 1)")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_94)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.label_95 = QLabel(self.layoutWidget)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(60, 60))
        self.label_95.setMaximumSize(QSize(50, 50))
        self.label_95.setFont(font1)
        self.label_95.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_95.setScaledContents(True)
        self.label_95.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_95)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_96 = QLabel(self.layoutWidget)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(50, 28))
        self.label_96.setMaximumSize(QSize(50, 28))
        self.label_96.setFont(font1)
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_96)

        self.label_97 = QLabel(self.layoutWidget)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(50, 15))
        self.label_97.setMaximumSize(QSize(50, 15))
        self.label_97.setFont(font1)
        self.label_97.setStyleSheet(u"background-color: rgb(229, 223, 105)")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_97)


        self.horizontalLayout_6.addLayout(self.verticalLayout_11)

        self.label_98 = QLabel(self.layoutWidget)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(60, 60))
        self.label_98.setMaximumSize(QSize(50, 50))
        self.label_98.setFont(font1)
        self.label_98.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_98.setScaledContents(True)
        self.label_98.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_98)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_99 = QLabel(self.layoutWidget)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(50, 28))
        self.label_99.setMaximumSize(QSize(50, 28))
        self.label_99.setFont(font1)
        self.label_99.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_99)

        self.label_100 = QLabel(self.layoutWidget)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(50, 15))
        self.label_100.setMaximumSize(QSize(50, 15))
        self.label_100.setFont(font1)
        self.label_100.setStyleSheet(u"background-color: rgb(187, 187, 187)")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_100)


        self.horizontalLayout_30.addLayout(self.verticalLayout_12)

        self.label_101 = QLabel(self.layoutWidget)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(60, 60))
        self.label_101.setMaximumSize(QSize(50, 50))
        self.label_101.setFont(font1)
        self.label_101.setPixmap(QPixmap(u"images/flowers/gardenia.png"))
        self.label_101.setScaledContents(True)
        self.label_101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_101)


        self.verticalLayout_2.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_102 = QLabel(self.layoutWidget)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(50, 28))
        self.label_102.setMaximumSize(QSize(50, 28))
        self.label_102.setFont(font1)
        self.label_102.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_102)

        self.label_103 = QLabel(self.layoutWidget)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(50, 15))
        self.label_103.setMaximumSize(QSize(50, 15))
        self.label_103.setFont(font1)
        self.label_103.setStyleSheet(u"background-color: rgb(227, 58, 91)")
        self.label_103.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_103)


        self.horizontalLayout_31.addLayout(self.verticalLayout_13)

        self.label_104 = QLabel(self.layoutWidget)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(60, 60))
        self.label_104.setMaximumSize(QSize(50, 50))
        self.label_104.setFont(font1)
        self.label_104.setPixmap(QPixmap(u"images/flowers/hibiscus.png"))
        self.label_104.setScaledContents(True)
        self.label_104.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_104)


        self.verticalLayout_2.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_105 = QLabel(self.layoutWidget)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(50, 28))
        self.label_105.setMaximumSize(QSize(50, 28))
        self.label_105.setFont(font1)
        self.label_105.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_105)

        self.label_106 = QLabel(self.layoutWidget)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(50, 15))
        self.label_106.setMaximumSize(QSize(50, 15))
        self.label_106.setFont(font1)
        self.label_106.setStyleSheet(u"background-color: rgb(169, 177, 232)")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_106)


        self.horizontalLayout_32.addLayout(self.verticalLayout_14)

        self.label_107 = QLabel(self.layoutWidget)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(60, 60))
        self.label_107.setMaximumSize(QSize(50, 50))
        self.label_107.setFont(font1)
        self.label_107.setPixmap(QPixmap(u"images/flowers/chrysanthemum.png"))
        self.label_107.setScaledContents(True)
        self.label_107.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_107)


        self.verticalLayout_2.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_108 = QLabel(self.layoutWidget)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(50, 28))
        self.label_108.setMaximumSize(QSize(50, 28))
        self.label_108.setFont(font1)
        self.label_108.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_108)

        self.label_109 = QLabel(self.layoutWidget)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(50, 15))
        self.label_109.setMaximumSize(QSize(50, 15))
        self.label_109.setFont(font1)
        self.label_109.setStyleSheet(u"background-color: rgb(153, 69, 253)")
        self.label_109.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_109)


        self.horizontalLayout_33.addLayout(self.verticalLayout_15)

        self.label_110 = QLabel(self.layoutWidget)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(60, 60))
        self.label_110.setMaximumSize(QSize(50, 50))
        self.label_110.setFont(font1)
        self.label_110.setPixmap(QPixmap(u"images/flowers/daisy.png"))
        self.label_110.setScaledContents(True)
        self.label_110.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_110)


        self.verticalLayout_2.addLayout(self.horizontalLayout_33)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_111 = QLabel(self.layoutWidget)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(50, 28))
        self.label_111.setMaximumSize(QSize(50, 28))
        self.label_111.setFont(font1)
        self.label_111.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_111)

        self.label_112 = QLabel(self.layoutWidget)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(50, 15))
        self.label_112.setMaximumSize(QSize(50, 15))
        self.label_112.setFont(font1)
        self.label_112.setStyleSheet(u"background-color: rgb(216, 158, 221)")
        self.label_112.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_112)


        self.horizontalLayout_4.addLayout(self.verticalLayout_16)

        self.label_113 = QLabel(self.layoutWidget)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(60, 60))
        self.label_113.setMaximumSize(QSize(50, 50))
        self.label_113.setFont(font1)
        self.label_113.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_113.setScaledContents(True)
        self.label_113.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_113)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_114 = QLabel(self.layoutWidget)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(50, 28))
        self.label_114.setMaximumSize(QSize(50, 28))
        self.label_114.setFont(font1)
        self.label_114.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_114)

        self.label_115 = QLabel(self.layoutWidget)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(50, 15))
        self.label_115.setMaximumSize(QSize(50, 15))
        self.label_115.setFont(font1)
        self.label_115.setStyleSheet(u"background-color: rgb(176, 197, 122)")
        self.label_115.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_115)


        self.horizontalLayout_7.addLayout(self.verticalLayout_17)

        self.label_116 = QLabel(self.layoutWidget)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(60, 60))
        self.label_116.setMaximumSize(QSize(50, 50))
        self.label_116.setFont(font1)
        self.label_116.setPixmap(QPixmap(u"images/flowers/lily.png"))
        self.label_116.setScaledContents(True)
        self.label_116.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_116)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_117 = QLabel(self.layoutWidget)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(50, 28))
        self.label_117.setMaximumSize(QSize(50, 28))
        self.label_117.setFont(font1)
        self.label_117.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_117)

        self.label_118 = QLabel(self.layoutWidget)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(50, 15))
        self.label_118.setMaximumSize(QSize(50, 15))
        self.label_118.setFont(font1)
        self.label_118.setStyleSheet(u"background-color: rgb(106, 135, 89)")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_118)


        self.horizontalLayout_34.addLayout(self.verticalLayout_18)

        self.label_119 = QLabel(self.layoutWidget)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(60, 60))
        self.label_119.setMaximumSize(QSize(50, 50))
        self.label_119.setFont(font1)
        self.label_119.setPixmap(QPixmap(u"images/flowers/lotus.png"))
        self.label_119.setScaledContents(True)
        self.label_119.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_119)


        self.verticalLayout_3.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_120 = QLabel(self.layoutWidget)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(50, 28))
        self.label_120.setMaximumSize(QSize(50, 28))
        self.label_120.setFont(font1)
        self.label_120.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_120)

        self.label_121 = QLabel(self.layoutWidget)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(50, 15))
        self.label_121.setMaximumSize(QSize(50, 15))
        self.label_121.setFont(font1)
        self.label_121.setStyleSheet(u"background-color: rgb(28, 77, 183)")
        self.label_121.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_121)


        self.horizontalLayout_35.addLayout(self.verticalLayout_19)

        self.label_122 = QLabel(self.layoutWidget)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(60, 60))
        self.label_122.setMaximumSize(QSize(50, 50))
        self.label_122.setFont(font1)
        self.label_122.setPixmap(QPixmap(u"images/flowers/morningglory.png"))
        self.label_122.setScaledContents(True)
        self.label_122.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_122)


        self.verticalLayout_3.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_123 = QLabel(self.layoutWidget)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(50, 28))
        self.label_123.setMaximumSize(QSize(50, 28))
        self.label_123.setFont(font1)
        self.label_123.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_123)

        self.label_124 = QLabel(self.layoutWidget)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(50, 15))
        self.label_124.setMaximumSize(QSize(50, 15))
        self.label_124.setFont(font1)
        self.label_124.setStyleSheet(u"background-color: rgb(249, 245, 138)")
        self.label_124.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_124)


        self.horizontalLayout_36.addLayout(self.verticalLayout_20)

        self.label_125 = QLabel(self.layoutWidget)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(60, 60))
        self.label_125.setMaximumSize(QSize(50, 50))
        self.label_125.setFont(font1)
        self.label_125.setPixmap(QPixmap(u"images/flowers/chrysanthemum.png"))
        self.label_125.setScaledContents(True)
        self.label_125.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_125)


        self.verticalLayout_3.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_126 = QLabel(self.layoutWidget)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(50, 28))
        self.label_126.setMaximumSize(QSize(50, 28))
        self.label_126.setFont(font1)
        self.label_126.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_126)

        self.label_127 = QLabel(self.layoutWidget)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(50, 15))
        self.label_127.setMaximumSize(QSize(50, 15))
        self.label_127.setFont(font1)
        self.label_127.setStyleSheet(u"background-color: rgb(224, 189, 213)")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_127)


        self.horizontalLayout_37.addLayout(self.verticalLayout_21)

        self.label_128 = QLabel(self.layoutWidget)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(60, 60))
        self.label_128.setMaximumSize(QSize(50, 50))
        self.label_128.setFont(font1)
        self.label_128.setPixmap(QPixmap(u"images/flowers/daisy.png"))
        self.label_128.setScaledContents(True)
        self.label_128.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_128)


        self.verticalLayout_3.addLayout(self.horizontalLayout_37)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_129 = QLabel(self.layoutWidget)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(50, 28))
        self.label_129.setMaximumSize(QSize(50, 28))
        self.label_129.setFont(font1)
        self.label_129.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_129)

        self.label_130 = QLabel(self.layoutWidget)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(50, 15))
        self.label_130.setMaximumSize(QSize(50, 15))
        self.label_130.setFont(font1)
        self.label_130.setStyleSheet(u"background-color: rgb(210, 111, 173)")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_130)


        self.horizontalLayout_8.addLayout(self.verticalLayout_23)

        self.label_131 = QLabel(self.layoutWidget)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(60, 60))
        self.label_131.setMaximumSize(QSize(50, 50))
        self.label_131.setFont(font1)
        self.label_131.setPixmap(QPixmap(u"images/flowers/peony.png"))
        self.label_131.setScaledContents(True)
        self.label_131.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_131)


        self.verticalLayout_22.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_132 = QLabel(self.layoutWidget)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(50, 28))
        self.label_132.setMaximumSize(QSize(50, 28))
        self.label_132.setFont(font1)
        self.label_132.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_132)

        self.label_133 = QLabel(self.layoutWidget)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(50, 15))
        self.label_133.setMaximumSize(QSize(50, 15))
        self.label_133.setFont(font1)
        self.label_133.setStyleSheet(u"background-color: rgb(185, 73, 79)")
        self.label_133.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_133)


        self.horizontalLayout_9.addLayout(self.verticalLayout_24)

        self.label_134 = QLabel(self.layoutWidget)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(60, 60))
        self.label_134.setMaximumSize(QSize(50, 50))
        self.label_134.setFont(font1)
        self.label_134.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_134.setScaledContents(True)
        self.label_134.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_134)


        self.verticalLayout_22.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_135 = QLabel(self.layoutWidget)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(50, 28))
        self.label_135.setMaximumSize(QSize(50, 28))
        self.label_135.setFont(font1)
        self.label_135.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_135)

        self.label_136 = QLabel(self.layoutWidget)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(50, 15))
        self.label_136.setMaximumSize(QSize(50, 15))
        self.label_136.setFont(font1)
        self.label_136.setStyleSheet(u"background-color: rgb(120, 0, 20)")
        self.label_136.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_136)


        self.horizontalLayout_38.addLayout(self.verticalLayout_25)

        self.label_137 = QLabel(self.layoutWidget)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMinimumSize(QSize(60, 60))
        self.label_137.setMaximumSize(QSize(50, 50))
        self.label_137.setFont(font1)
        self.label_137.setPixmap(QPixmap(u"images/flowers/camellia.png"))
        self.label_137.setScaledContents(True)
        self.label_137.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_137)


        self.verticalLayout_22.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_138 = QLabel(self.layoutWidget)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(50, 28))
        self.label_138.setMaximumSize(QSize(50, 28))
        self.label_138.setFont(font1)
        self.label_138.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_138)

        self.label_139 = QLabel(self.layoutWidget)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(50, 15))
        self.label_139.setMaximumSize(QSize(50, 15))
        self.label_139.setFont(font1)
        self.label_139.setStyleSheet(u"background-color: rgb(181, 97, 127)")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_139)


        self.horizontalLayout_39.addLayout(self.verticalLayout_26)

        self.label_140 = QLabel(self.layoutWidget)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(60, 60))
        self.label_140.setMaximumSize(QSize(50, 50))
        self.label_140.setFont(font1)
        self.label_140.setPixmap(QPixmap(u"images/flowers/bougainvillea.png"))
        self.label_140.setScaledContents(True)
        self.label_140.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_140)


        self.verticalLayout_22.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_141 = QLabel(self.layoutWidget)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(50, 28))
        self.label_141.setMaximumSize(QSize(50, 28))
        self.label_141.setFont(font1)
        self.label_141.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_141)

        self.label_142 = QLabel(self.layoutWidget)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(50, 15))
        self.label_142.setMaximumSize(QSize(50, 15))
        self.label_142.setFont(font1)
        self.label_142.setStyleSheet(u"background-color: rgb(205, 134, 18)")
        self.label_142.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_142)


        self.horizontalLayout_40.addLayout(self.verticalLayout_27)

        self.label_143 = QLabel(self.layoutWidget)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(60, 60))
        self.label_143.setMaximumSize(QSize(50, 50))
        self.label_143.setFont(font1)
        self.label_143.setPixmap(QPixmap(u"images/flowers/sunflower.png"))
        self.label_143.setScaledContents(True)
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_143)


        self.verticalLayout_22.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_144 = QLabel(self.layoutWidget)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(50, 28))
        self.label_144.setMaximumSize(QSize(50, 28))
        self.label_144.setFont(font1)
        self.label_144.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_144)

        self.label_145 = QLabel(self.layoutWidget)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(50, 15))
        self.label_145.setMaximumSize(QSize(50, 15))
        self.label_145.setFont(font1)
        self.label_145.setStyleSheet(u"background-color: rgb(240, 96, 140)")
        self.label_145.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_145)


        self.horizontalLayout_41.addLayout(self.verticalLayout_28)

        self.image_label = QLabel(self.layoutWidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(60, 60))
        self.image_label.setMaximumSize(QSize(50, 50))
        self.image_label.setFont(font1)
        self.image_label.setPixmap(QPixmap(u"images/flowers/daisy.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.image_label)


        self.verticalLayout_22.addLayout(self.horizontalLayout_41)


        self.horizontalLayout.addLayout(self.verticalLayout_22)

        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"\u5173\u4e8e\u672c\u8f6f\u4ef6", None))
#if QT_CONFIG(tooltip)
        AboutWindow.setToolTip(QCoreApplication.translate("AboutWindow", u"\u53f3\u952e\u5173\u95ed\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("AboutWindow", u"\u672c\u8f6f\u4ef6\u53ef\u4ee5\u8fdb\u884c\u4ee5\u4e0b24\u7c7b\u82b1\u6735\u56fe\u50cf\u5206\u7c7b", None))
        self.label_13.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">\u672c\u9879\u76ee\u5b8c\u5168\u5f00\u6e90\uff0c\u9879\u76ee\u5e93\u5730\u5740\uff1a</span><a href=\"https://github.com/Rvioleck/FlowerClassification\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Rvioleck/FlowerClassification</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("AboutWindow", u"\u8f6f\u4ef6\u4f7f\u7528\u8bf4\u660e", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("AboutWindow", u"...", None))
        self.label_75.setText(QCoreApplication.translate("AboutWindow", u"\u675c\u9e43\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_76.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(222, 60, 60)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.azalea.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/azalea.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_78.setText(QCoreApplication.translate("AboutWindow", u"\u53f6\u5b50\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_79.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(255, 148, 217)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_80.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/bougainvillea.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_81.setText(QCoreApplication.translate("AboutWindow", u"\u5c71\u8336\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_82.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(245, 156, 185)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_83.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/camellia.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_84.setText(QCoreApplication.translate("AboutWindow", u"\u5eb7\u4e43\u99a8", None))
#if QT_CONFIG(tooltip)
        self.label_85.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(218, 187, 171)", None))
#endif // QT_CONFIG(tooltip)
        self.label_90.setText(QCoreApplication.translate("AboutWindow", u"\u83ca  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_91.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(236, 181, 1)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_92.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/chrysanthemum.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_87.setText(QCoreApplication.translate("AboutWindow", u"\u96cf  \u83ca", None))
#if QT_CONFIG(tooltip)
        self.label_88.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(241, 203, 6)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_89.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/daisy.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_93.setText(QCoreApplication.translate("AboutWindow", u"\u84b2\u516c\u82f1", None))
#if QT_CONFIG(tooltip)
        self.label_94.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(96, 67, 1)", None))
#endif // QT_CONFIG(tooltip)
        self.label_96.setText(QCoreApplication.translate("AboutWindow", u"\u6842  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_97.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(229, 223, 105)", None))
#endif // QT_CONFIG(tooltip)
        self.label_99.setText(QCoreApplication.translate("AboutWindow", u"\u6800\u5b50\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_100.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(187, 187, 187)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_101.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/gardenia.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_102.setText(QCoreApplication.translate("AboutWindow", u"\u6728\u69ff\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_103.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(227, 58, 91))", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_104.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/hibiscus.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_105.setText(QCoreApplication.translate("AboutWindow", u"\u7ee3\u7403\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_106.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(169, 177, 232)", None))
#endif // QT_CONFIG(tooltip)
        self.label_108.setText(QCoreApplication.translate("AboutWindow", u"\u9e22\u5c3e\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_109.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(153, 69, 253)", None))
#endif // QT_CONFIG(tooltip)
        self.label_111.setText(QCoreApplication.translate("AboutWindow", u"\u4e01\u9999\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_112.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(216, 158, 221)", None))
#endif // QT_CONFIG(tooltip)
        self.label_114.setText(QCoreApplication.translate("AboutWindow", u"\u767e\u5408\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_115.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(176, 197, 122)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_116.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/lily.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_117.setText(QCoreApplication.translate("AboutWindow", u"\u8377  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_118.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(106, 135, 89)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_119.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/lotus.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_120.setText(QCoreApplication.translate("AboutWindow", u"\u7275\u725b\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_121.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(28, 77, 183)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_122.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/morningglory.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_123.setText(QCoreApplication.translate("AboutWindow", u"\u6c34\u4ed9\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_124.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(249, 245, 138)", None))
#endif // QT_CONFIG(tooltip)
        self.label_126.setText(QCoreApplication.translate("AboutWindow", u"\u6843  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_127.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(224, 189, 213)", None))
#endif // QT_CONFIG(tooltip)
        self.label_129.setText(QCoreApplication.translate("AboutWindow", u"\u7261\u4e39\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_130.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(210, 111, 173)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_131.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/peony.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_132.setText(QCoreApplication.translate("AboutWindow", u"\u8774\u8776\u5170", None))
#if QT_CONFIG(tooltip)
        self.label_133.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(185, 73, 79)", None))
#endif // QT_CONFIG(tooltip)
        self.label_135.setText(QCoreApplication.translate("AboutWindow", u"\u73ab\u7470\u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_136.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(120, 0, 20))", None))
#endif // QT_CONFIG(tooltip)
        self.label_138.setText(QCoreApplication.translate("AboutWindow", u"\u6a31  \u82b1", None))
#if QT_CONFIG(tooltip)
        self.label_139.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(181, 97, 127)", None))
#endif // QT_CONFIG(tooltip)
        self.label_141.setText(QCoreApplication.translate("AboutWindow", u"\u5411\u65e5\u8475", None))
#if QT_CONFIG(tooltip)
        self.label_142.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(205, 134, 18)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_143.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><img src=\":/big/sunflower.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_144.setText(QCoreApplication.translate("AboutWindow", u"\u90c1\u91d1\u9999", None))
#if QT_CONFIG(tooltip)
        self.label_145.setToolTip(QCoreApplication.translate("AboutWindow", u"RGB(240, 96, 140))", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

