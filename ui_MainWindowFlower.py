# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowFlower.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 670)
        MainWindow.setMinimumSize(QSize(900, 670))
        MainWindow.setMaximumSize(QSize(900, 670))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"images/AI\u8bc6\u522b.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.170455 rgba(82, 169, 220, 204), stop:1 rgba(217, 239, 231, 255));\n"
"border-radius:5px;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.myModelAction = QAction(MainWindow)
        self.myModelAction.setObjectName(u"myModelAction")
        self.denseNet121Action = QAction(MainWindow)
        self.denseNet121Action.setObjectName(u"denseNet121Action")
        self.efficientNetB0Action = QAction(MainWindow)
        self.efficientNetB0Action.setObjectName(u"efficientNetB0Action")
        self.vggAction = QAction(MainWindow)
        self.vggAction.setObjectName(u"vggAction")
        self.inceptionAction = QAction(MainWindow)
        self.inceptionAction.setObjectName(u"inceptionAction")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon1 = QIcon()
        icon1.addFile(u"images/\u65b0\u5efa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon1)
        font = QFont()
        self.actionNew.setFont(font)
        self.actionNew.setShortcutContext(Qt.WidgetWithChildrenShortcut)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon2 = QIcon()
        icon2.addFile(u"images/\u6253\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setFont(font)
        self.actionOpen.setShortcutContext(Qt.WidgetWithChildrenShortcut)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon3 = QIcon()
        icon3.addFile(u"images/\u5173\u95ed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose.setIcon(icon3)
        font1 = QFont()
        font1.setPointSize(10)
        self.actionClose.setFont(font1)
        self.actionCNN = QAction(MainWindow)
        self.actionCNN.setObjectName(u"actionCNN")
        icon4 = QIcon()
        icon4.addFile(u"images/\u6298\u7ebf\u56fe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCNN.setIcon(icon4)
        self.mobileNetAction = QAction(MainWindow)
        self.mobileNetAction.setObjectName(u"mobileNetAction")
        self.efficientNetB4Action = QAction(MainWindow)
        self.efficientNetB4Action.setObjectName(u"efficientNetB4Action")
        self.efficientNetB7Action = QAction(MainWindow)
        self.efficientNetB7Action.setObjectName(u"efficientNetB7Action")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon5 = QIcon()
        icon5.addFile(u"images/\u4fdd\u5b58.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionClassify = QAction(MainWindow)
        self.actionClassify.setObjectName(u"actionClassify")
        icon6 = QIcon()
        icon6.addFile(u"images/\u4eba\u5de5\u667a\u80fd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClassify.setIcon(icon6)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(True)
        self.actionClassify.setFont(font2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 901, 591))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.tabWidget.setFont(font3)
        self.tabWidget.setStyleSheet(u"#tabWidget{\n"
"background-color:rgb(202,229,230)\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setMovable(True)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setStyleSheet(u"#tab1{\n"
"border-radius: 8px;\n"
"background-color: qlineargradient(spread:pad, x1:0.358, y1:0.397909, x2:0.823, y2:0.704864, stop:0 rgba(86, 140, 209, 157), stop:0.903409 rgba(228, 237, 209, 199));\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 169, 220, 168), stop:1 rgba(194, 239, 224, 199))\n"
"/*rgb(244, 248, 255)*/\n"
"}")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 13, 341, 331))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.groupBox.setFont(font4)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.imageLabel = QLabel(self.groupBox)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(50, 100, 224, 224))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(224, 224))
        self.imageLabel.setMaximumSize(QSize(224, 224))
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(16)
        font5.setBold(True)
        self.imageLabel.setFont(font5)
        self.imageLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setPixmap(QPixmap(u"images/\u4e0a\u4f20\u56fe\u7247.png"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setWordWrap(False)
        self.chooseButton = QPushButton(self.groupBox)
        self.chooseButton.setObjectName(u"chooseButton")
        self.chooseButton.setGeometry(QRect(10, 60, 32, 32))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chooseButton.sizePolicy().hasHeightForWidth())
        self.chooseButton.setSizePolicy(sizePolicy1)
        self.chooseButton.setMinimumSize(QSize(32, 32))
        self.chooseButton.setMaximumSize(QSize(32, 32))
        self.chooseButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"images/\u5bfc\u5165\u56fe\u7247.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chooseButton.setIcon(icon7)
        self.chooseButton.setIconSize(QSize(28, 28))
        self.chooseButton.setFlat(True)
        self.nameEdit = QLineEdit(self.groupBox)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(50, 64, 261, 25))
        self.nameEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.nameEdit.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"border-radius: 5px;\n"
"border: 1px outset rgb(199, 216, 255);\n"
"padding: 3px")
        self.nameEdit.setReadOnly(True)
        self.pathLabel = QLabel(self.groupBox)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setGeometry(QRect(50, 20, 261, 41))
        sizePolicy.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy)
        self.pathLabel.setMinimumSize(QSize(0, 30))
        self.pathLabel.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(10)
        self.pathLabel.setFont(font6)
        self.pathLabel.setTextFormat(Qt.RichText)
        self.pathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pathLabel.setWordWrap(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 31, 16))
        self.groupBox_4 = QGroupBox(self.tab1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 355, 341, 201))
        self.groupBox_4.setFont(font4)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.groupBox_4.setFlat(True)
        self.imageTextEdit = QTextEdit(self.groupBox_4)
        self.imageTextEdit.setObjectName(u"imageTextEdit")
        self.imageTextEdit.setGeometry(QRect(10, 26, 171, 121))
        self.imageTextEdit.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"border-radius: 5px;\n"
"border: 1px outset rgb(199, 216, 255);\n"
"padding: 3px")
        self.imageTextEdit.setReadOnly(True)
        self.saveButton = QPushButton(self.groupBox_4)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(210, 30, 121, 31))
        self.saveButton.setStyleSheet(u"QPushButton\n"
"                        {\n"
"                        background-color:transparent;\n"
"                        border:2px solid rgb(59,154,156);\n"
"                        border-radius:5px;\n"
"                        color:black\n"
"                        }\n"
"                        QPushButton:hover\n"
"                        {\n"
"                        background-color:rgb(234,250,255);\n"
"                        border:2px solid rgb(7,130,245);\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        }\n"
"                        QPushButton:hover:pressed\n"
"                        {\n"
"                        border:2px solid #5F92B2;\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        padding-right:3px;\n"
"                        padding-top:3px;\n"
"                        }\n"
"                    ")
        icon8 = QIcon()
        icon8.addFile(u"images/\u4fdd\u5b58\u56fe\u7247.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon8)
        self.saveButton.setIconSize(QSize(20, 20))
        self.saveNameEdit = QLineEdit(self.groupBox_4)
        self.saveNameEdit.setObjectName(u"saveNameEdit")
        self.saveNameEdit.setGeometry(QRect(210, 70, 121, 25))
        self.saveNameEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.saveNameEdit.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"border-radius: 5px;\n"
"border: 1px outset rgb(199, 216, 255);\n"
"padding: 3px")
        self.saveNameEdit.setFrame(True)
        self.savePathLineEdit_2 = QLineEdit(self.groupBox_4)
        self.savePathLineEdit_2.setObjectName(u"savePathLineEdit_2")
        self.savePathLineEdit_2.setGeometry(QRect(210, 110, 121, 81))
        self.savePathLineEdit_2.setCursor(QCursor(Qt.IBeamCursor))
        self.savePathLineEdit_2.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"border-radius: 5px;\n"
"border: 1px outset rgb(199, 216, 255);\n"
"padding: 3px")
        self.savePathLineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.savePathLineEdit_2.setReadOnly(True)
        self.savePathLineEdit_2.setClearButtonEnabled(True)
        self.line = QFrame(self.groupBox_4)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(190, 20, 10, 170))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.getDirectoryButton_2 = QToolButton(self.groupBox_4)
        self.getDirectoryButton_2.setObjectName(u"getDirectoryButton_2")
        self.getDirectoryButton_2.setGeometry(QRect(304, 166, 24, 22))
        self.getDirectoryButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"images/\u6587\u4ef6\u5939.png", QSize(), QIcon.Normal, QIcon.Off)
        self.getDirectoryButton_2.setIcon(icon9)
        self.getDirectoryButton_2.setIconSize(QSize(24, 24))
        self.getDirectoryButton_2.setAutoRaise(True)
        self.cutButton = QPushButton(self.groupBox_4)
        self.cutButton.setObjectName(u"cutButton")
        self.cutButton.setGeometry(QRect(9, 160, 81, 30))
        self.cutButton.setStyleSheet(u"QPushButton\n"
"                        {\n"
"                        background-color:transparent;\n"
"                        border:2px solid rgb(59,154,156);\n"
"                        border-radius:5px;\n"
"                        color:black\n"
"                        }\n"
"                        QPushButton:hover\n"
"                        {\n"
"                        background-color:rgb(234,250,255);\n"
"                        border:2px solid rgb(7,130,245);\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        }\n"
"                        QPushButton:hover:pressed\n"
"                        {\n"
"                        border:2px solid #5F92B2;\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        padding-right:3px;\n"
"                        padding-top:3px;\n"
"                        }\n"
"                    ")
        icon10 = QIcon()
        icon10.addFile(u"images/\u88c1\u526a\u65cb\u8f6c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cutButton.setIcon(icon10)
        self.cutButton.setIconSize(QSize(24, 24))
        self.resetButton = QPushButton(self.groupBox_4)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(100, 160, 81, 31))
        self.resetButton.setStyleSheet(u"QPushButton\n"
"                        {\n"
"                        background-color:transparent;\n"
"                        border:2px solid rgb(59,154,156);\n"
"                        border-radius:5px;\n"
"                        color:black\n"
"                        }\n"
"                        QPushButton:hover\n"
"                        {\n"
"                        background-color:rgb(234,250,255);\n"
"                        border:2px solid rgb(7,130,245);\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        }\n"
"                        QPushButton:hover:pressed\n"
"                        {\n"
"                        border:2px solid #5F92B2;\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        padding-right:3px;\n"
"                        padding-top:3px;\n"
"                        }\n"
"                    ")
        icon11 = QIcon()
        icon11.addFile(u"images/\u590d\u4f4d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon11)
        self.resetButton.setIconSize(QSize(21, 21))
        self.groupBox_5 = QGroupBox(self.tab1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(380, 10, 491, 541))
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.groupBox_5.setFont(font7)
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.groupBox_5.setFlat(True)
        self.layoutWidget = QWidget(self.groupBox_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 26, 451, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.predictButton = QPushButton(self.layoutWidget)
        self.predictButton.setObjectName(u"predictButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.predictButton.sizePolicy().hasHeightForWidth())
        self.predictButton.setSizePolicy(sizePolicy2)
        self.predictButton.setMinimumSize(QSize(60, 0))
        self.predictButton.setMaximumSize(QSize(60, 25))
        self.predictButton.setLayoutDirection(Qt.LeftToRight)
        self.predictButton.setAutoFillBackground(False)
        self.predictButton.setStyleSheet(u"QPushButton\n"
"                        {\n"
"                        background-color:transparent;\n"
"                        border:2px solid #0782f5;\n"
"                        border-radius:5px;\n"
"                        color:black\n"
"                        }\n"
"                        QPushButton:hover\n"
"                        {\n"
"                        /*\u80cc\u666f\u989c\u8272*/\n"
"                        background-color:rgb(170, 200, 255);\n"
"                        /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/\n"
"                        }\n"
"                        QPushButton:hover:pressed\n"
"                        {\n"
"                        border:2px solid #5F92B2;\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        padding-right:3px;\n"
"                        padding-top:3px;\n"
"                        }\n"
"                    ")
        self.predictButton.setIcon(icon)
        self.predictButton.setIconSize(QSize(24, 24))
        self.predictButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.predictButton)

        self.resultLabel = QLabel(self.layoutWidget)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy3)
        self.resultLabel.setMinimumSize(QSize(20, 25))
        self.resultLabel.setMaximumSize(QSize(600, 25))
        self.resultLabel.setScaledContents(True)
        self.resultLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.resultLabel)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(3, 0))
        self.label_3.setMaximumSize(QSize(3, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.resultLabel_2 = QLabel(self.layoutWidget)
        self.resultLabel_2.setObjectName(u"resultLabel_2")
        sizePolicy1.setHeightForWidth(self.resultLabel_2.sizePolicy().hasHeightForWidth())
        self.resultLabel_2.setSizePolicy(sizePolicy1)
        self.resultLabel_2.setMinimumSize(QSize(25, 25))
        self.resultLabel_2.setMaximumSize(QSize(25, 25))
        self.resultLabel_2.setScaledContents(True)
        self.resultLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.resultLabel_2)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 441, 441))
        self.label_4.setPixmap(QPixmap(u"images/rongzi.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.line_3 = QFrame(self.groupBox_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 70, 451, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.tab1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(355, 28, 20, 521))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.clearButton = QToolButton(self.tab1)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(20, 331, 31, 31))
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u"../../main/images/clear-l.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon12)
        self.clearButton.setIconSize(QSize(40, 40))
        self.clearButton.setAutoRaise(True)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tab2.setStyleSheet(u"#tab2{\n"
"border-radius: 8px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0511364 rgba(86, 140, 209, 97), stop:1 rgba(228, 237, 209, 175));\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 169, 220, 168), stop:1 rgba(194, 239, 224, 199))\n"
"/*rgb(244, 248, 255)*/\n"
"}")
        self.tableWidget = QTableWidget(self.tab2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font8 = QFont()
        font8.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font8.setPointSize(11)
        font8.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font8);
        __qtablewidgetitem.setIcon(icon9);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon13 = QIcon()
        icon13.addFile(u"images/\u56fe\u7247.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8);
        __qtablewidgetitem1.setIcon(icon13);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon14 = QIcon()
        icon14.addFile(u"images/\u82b1\u6735.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font8);
        __qtablewidgetitem2.setIcon(icon14);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 431, 521))
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"gridline-color: rgb(85, 85, 0);\n"
"alternate-background-color:rgb(170, 0, 0);\n"
"selection-color:red;\n"
"selection-background-color: rgb(191,211,238);\n"
"border:1px solid rgb(0, 85, 0);\n"
"\n"
"\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setIconSize(QSize(24, 24))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.clearTableButton = QPushButton(self.tab2)
        self.clearTableButton.setObjectName(u"clearTableButton")
        self.clearTableButton.setGeometry(QRect(404, 527, 30, 30))
        sizePolicy1.setHeightForWidth(self.clearTableButton.sizePolicy().hasHeightForWidth())
        self.clearTableButton.setSizePolicy(sizePolicy1)
        self.clearTableButton.setMinimumSize(QSize(30, 30))
        self.clearTableButton.setMaximumSize(QSize(30, 30))
        self.clearTableButton.setLayoutDirection(Qt.LeftToRight)
        self.clearTableButton.setAutoFillBackground(False)
        self.clearTableButton.setStyleSheet(u"QPushButton:hover\n"
"                 {\n"
"                 background-color: rgb(224, 255, 254);\n"
"                 border:2px solid #5F92B2;\n"
"                 border-radius:5px;\n"
"                 color:white;\n"
"                 }\n"
"             ")
        icon15 = QIcon()
        icon15.addFile(u"images/\u5220\u9664.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearTableButton.setIcon(icon15)
        self.clearTableButton.setIconSize(QSize(24, 24))
        self.clearTableButton.setFlat(True)
        self.groupBox_2 = QGroupBox(self.tab2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(450, 10, 421, 131))
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 50, 401, 72))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.savePathLineEdit = QLineEdit(self.layoutWidget1)
        self.savePathLineEdit.setObjectName(u"savePathLineEdit")
        self.savePathLineEdit.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"border-radius: 5px;\n"
"border: 1px inset rgb(199, 216, 255);\n"
"padding: 3px")

        self.horizontalLayout.addWidget(self.savePathLineEdit)

        self.getDirectoryButton = QToolButton(self.layoutWidget1)
        self.getDirectoryButton.setObjectName(u"getDirectoryButton")
        self.getDirectoryButton.setIcon(icon9)
        self.getDirectoryButton.setIconSize(QSize(24, 24))
        self.getDirectoryButton.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.getDirectoryButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.batchRenameRadioButton = QRadioButton(self.layoutWidget1)
        self.batchRenameRadioButton.setObjectName(u"batchRenameRadioButton")

        self.horizontalLayout_2.addWidget(self.batchRenameRadioButton)

        self.batchExportButton = QPushButton(self.layoutWidget1)
        self.batchExportButton.setObjectName(u"batchExportButton")
        sizePolicy2.setHeightForWidth(self.batchExportButton.sizePolicy().hasHeightForWidth())
        self.batchExportButton.setSizePolicy(sizePolicy2)
        self.batchExportButton.setMinimumSize(QSize(80, 25))
        self.batchExportButton.setMaximumSize(QSize(80, 25))
        self.batchExportButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.batchExportButton.setLayoutDirection(Qt.LeftToRight)
        self.batchExportButton.setAutoFillBackground(False)
        self.batchExportButton.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"                           QPushButton\n"
"                           {\n"
"                           /*\u5b57\u4f53\u4e3a\u5fae\u8f6f\u96c5\u9ed1*/\n"
"                           font-family:Microsoft Yahei;\n"
"                           /*\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272*/\n"
"                           color:white;\n"
"                           /*\u80cc\u666f\u989c\u8272*/\n"
"                           background-color:rgb(14 , 150 , 254);\n"
"                           /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a8\u50cf\u7d20*/\n"
"                           border-radius:8px;\n"
"                           }\n"
"\n"
"                           /*\u6309\u94ae\u505c\u7559\u6001*/\n"
"                           QPushButton:hover\n"
"                           {\n"
"                           /*\u80cc\u666f\u989c\u8272*/\n"
"                           background-color:rgb(170, 200, 255);\n"
"                           /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf"
                        "\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/\n"
"                           padding-right:3px;\n"
"                           /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/\n"
"                           padding-bottom:3px;\n"
"                           color:rgb(255, 255, 255);\n"
"                           }\n"
"\n"
"                           /*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"                           QPushButton:pressed\n"
"                           {\n"
"                           /*\u80cc\u666f\u989c\u8272*/\n"
"                           background-color:rgb(14 , 135 , 255);\n"
"                           /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/\n"
"                           padding-left:3px;\n"
"                           /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411"
                        "\u4e0b\u79fb\u52a83\u50cf\u7d20*/\n"
"                           padding-top:3px;\n"
"                           }\n"
"                       ")
        self.batchExportButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.batchExportButton)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.batchPredictButton = QPushButton(self.groupBox_2)
        self.batchPredictButton.setObjectName(u"batchPredictButton")
        self.batchPredictButton.setGeometry(QRect(150, 20, 110, 25))
        sizePolicy2.setHeightForWidth(self.batchPredictButton.sizePolicy().hasHeightForWidth())
        self.batchPredictButton.setSizePolicy(sizePolicy2)
        self.batchPredictButton.setMinimumSize(QSize(110, 25))
        self.batchPredictButton.setMaximumSize(QSize(110, 25))
        self.batchPredictButton.setLayoutDirection(Qt.LeftToRight)
        self.batchPredictButton.setAutoFillBackground(False)
        self.batchPredictButton.setStyleSheet(u"QPushButton\n"
"                        {\n"
"                        background-color:transparent;\n"
"                        border:2px solid #0782f5;\n"
"                        border-radius:5px;\n"
"                        color:black\n"
"                        }\n"
"                        QPushButton:hover\n"
"                        {\n"
"                        background-color:rgb(255, 248, 250);\n"
"                        border:2px solid #5F92B2;\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        }\n"
"                        QPushButton:hover:pressed\n"
"                        {\n"
"                        border:2px solid #5F92B2;\n"
"                        border-radius:5px;\n"
"                        color:black;\n"
"                        padding-right:3px;\n"
"                        padding-top:3px;\n"
"                        }\n"
"                    ")
        icon16 = QIcon()
        icon16.addFile(u"images/Image \u56fe\u50cf\u8bc6\u522b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.batchPredictButton.setIcon(icon16)
        self.batchPredictButton.setIconSize(QSize(24, 24))
        self.batchPredictButton.setFlat(False)
        self.batchImportLabel = QLabel(self.tab2)
        self.batchImportLabel.setObjectName(u"batchImportLabel")
        self.batchImportLabel.setGeometry(QRect(9, 477, 351, 21))
        font9 = QFont()
        font9.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font9.setPointSize(11)
        self.batchImportLabel.setFont(font9)
        self.batchChooseButton = QPushButton(self.tab2)
        self.batchChooseButton.setObjectName(u"batchChooseButton")
        self.batchChooseButton.setGeometry(QRect(370, 527, 30, 30))
        sizePolicy1.setHeightForWidth(self.batchChooseButton.sizePolicy().hasHeightForWidth())
        self.batchChooseButton.setSizePolicy(sizePolicy1)
        self.batchChooseButton.setMinimumSize(QSize(30, 30))
        self.batchChooseButton.setMaximumSize(QSize(30, 30))
        self.batchChooseButton.setStyleSheet(u"QPushButton:hover\n"
"                 {\n"
"                 background-color: rgb(224, 255, 254);\n"
"                 border:2px solid #5F92B2;\n"
"                 border-radius:5px;\n"
"                 color:white;\n"
"                 }\n"
"             ")
        icon17 = QIcon()
        icon17.addFile(u"images/\u5bfc\u5165.png", QSize(), QIcon.Normal, QIcon.Off)
        self.batchChooseButton.setIcon(icon17)
        self.batchChooseButton.setIconSize(QSize(24, 24))
        self.batchChooseButton.setFlat(True)
        self.statisticsTextEdit = QTextEdit(self.tab2)
        self.statisticsTextEdit.setObjectName(u"statisticsTextEdit")
        self.statisticsTextEdit.setGeometry(QRect(450, 150, 421, 401))
        self.statisticsTextEdit.setStyleSheet(u"background-color:rgb(234,250,255);\n"
"border-radius: 5px;\n"
"border: 1px outset rgb(199, 216, 255);\n"
"padding: 3px")
        self.statisticsTextEdit.setReadOnly(True)
        self.statisticsButton = QPushButton(self.tab2)
        self.statisticsButton.setObjectName(u"statisticsButton")
        self.statisticsButton.setGeometry(QRect(820, 520, 30, 30))
        sizePolicy1.setHeightForWidth(self.statisticsButton.sizePolicy().hasHeightForWidth())
        self.statisticsButton.setSizePolicy(sizePolicy1)
        self.statisticsButton.setMinimumSize(QSize(30, 30))
        self.statisticsButton.setMaximumSize(QSize(30, 30))
        self.statisticsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.statisticsButton.setStyleSheet(u"QPushButton:hover\n"
"                 {\n"
"                 background-color: rgb(224, 255, 254);\n"
"                 border:2px solid #5F92B2;\n"
"                 border-radius:5px;\n"
"                 color:white;\n"
"                 }\n"
"             ")
        icon18 = QIcon()
        icon18.addFile(u"images/\u5806\u53e0\u67f1\u72b6\u56fe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statisticsButton.setIcon(icon18)
        self.statisticsButton.setIconSize(QSize(24, 24))
        self.statisticsButton.setFlat(True)
        self.tabWidget.addTab(self.tab2, "")
        self.groupBox_2.raise_()
        self.tableWidget.raise_()
        self.clearTableButton.raise_()
        self.batchImportLabel.raise_()
        self.batchChooseButton.raise_()
        self.statisticsTextEdit.raise_()
        self.statisticsButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 30))
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(25)
        sizePolicy5.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy5)
        self.menubar.setMinimumSize(QSize(0, 30))
        self.menubar.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setFamilies([u"Microsoft YaHei"])
        font10.setPointSize(10)
        font10.setBold(False)
        self.menubar.setFont(font10)
        self.menubar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.170455 rgba(85,166,212, 133), stop:1 rgba(217, 239, 231, 255));\n"
"/*qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.170455 rgba(82, 169, 220, 204), stop:1 rgba(217, 239, 231, 255));*/\n"
"padding: 5px;\n"
"border-radius: 4px;\n"
"\n"
"")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setToolTipsVisible(True)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_M = QMenu(self.menubar)
        self.menu_M.setObjectName(u"menu_M")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        self.toolBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBar.setStyleSheet(u"/*#toolBar{*/\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.460227 rgba(144, 189, 222, 204), stop:1 rgba(217, 239, 231, 255));\n"
"height: 20px;\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(215, 238, 255);\n"
"padding: 3px\n"
"/*}*/\n"
"")
        self.toolBar.setAllowedAreas(Qt.BottomToolBarArea|Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_M.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menu_2.addAction(self.actionAbout)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionCNN)
        self.menu_M.addAction(self.efficientNetB7Action)
        self.menu_M.addAction(self.efficientNetB4Action)
        self.menu_M.addAction(self.efficientNetB0Action)
        self.menu_M.addSeparator()
        self.menu_M.addAction(self.mobileNetAction)
        self.menu_M.addAction(self.denseNet121Action)
        self.menu_M.addAction(self.inceptionAction)
        self.menu_M.addAction(self.vggAction)
        self.menu_M.addSeparator()
        self.menu_M.addAction(self.actionCNN)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCNN)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClassify)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u5206\u7c7b", None))
        self.myModelAction.setText(QCoreApplication.translate("MainWindow", u"MyModel", None))
#if QT_CONFIG(tooltip)
        self.myModelAction.setToolTip(QCoreApplication.translate("MainWindow", u"MyModel", None))
#endif // QT_CONFIG(tooltip)
        self.denseNet121Action.setText(QCoreApplication.translate("MainWindow", u"DenseNet121", None))
#if QT_CONFIG(tooltip)
        self.denseNet121Action.setToolTip(QCoreApplication.translate("MainWindow", u"DenseNet121", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.denseNet121Action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.efficientNetB0Action.setText(QCoreApplication.translate("MainWindow", u"EfficientNetB0", None))
#if QT_CONFIG(tooltip)
        self.efficientNetB0Action.setToolTip(QCoreApplication.translate("MainWindow", u"EfficientNetB0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.efficientNetB0Action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+0", None))
#endif // QT_CONFIG(shortcut)
        self.vggAction.setText(QCoreApplication.translate("MainWindow", u"VGG19", None))
#if QT_CONFIG(tooltip)
        self.vggAction.setToolTip(QCoreApplication.translate("MainWindow", u"VGG19", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.vggAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+G", None))
#endif // QT_CONFIG(shortcut)
        self.inceptionAction.setText(QCoreApplication.translate("MainWindow", u"InceptionV3", None))
#if QT_CONFIG(tooltip)
        self.inceptionAction.setToolTip(QCoreApplication.translate("MainWindow", u"InceptionV3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.inceptionAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa(&N)", None))
#if QT_CONFIG(tooltip)
        self.actionNew.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(&O)", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed(&C)", None))
        self.actionCNN.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7edf\u8ba1", None))
#if QT_CONFIG(tooltip)
        self.actionCNN.setToolTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7edf\u8ba1", None))
#endif // QT_CONFIG(tooltip)
        self.mobileNetAction.setText(QCoreApplication.translate("MainWindow", u"MobileNetV2", None))
#if QT_CONFIG(tooltip)
        self.mobileNetAction.setToolTip(QCoreApplication.translate("MainWindow", u"MobileNetV2", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.mobileNetAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.efficientNetB4Action.setText(QCoreApplication.translate("MainWindow", u"EfficientNetB4", None))
#if QT_CONFIG(tooltip)
        self.efficientNetB4Action.setToolTip(QCoreApplication.translate("MainWindow", u"EfficientNetB4", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.efficientNetB4Action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+4", None))
#endif // QT_CONFIG(shortcut)
        self.efficientNetB7Action.setText(QCoreApplication.translate("MainWindow", u"EfficientNetB7", None))
#if QT_CONFIG(tooltip)
        self.efficientNetB7Action.setToolTip(QCoreApplication.translate("MainWindow", u"EfficientNetB7", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.efficientNetB7Action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+7", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58(&S)", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClassify.setText(QCoreApplication.translate("MainWindow", u"\u6df1\u5ea6\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.actionClassify.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u8fdb\u884c</span><span style=\" font-size:10pt; font-weight:700;\">\u591a\u6a21\u578b</span><span style=\" font-size:10pt;\">\u52a0\u6743\u6df1\u5ea6\u8bc6\u522b</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u5165", None))
#if QT_CONFIG(tooltip)
        self.imageLabel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u53cc\u51fb\u9009\u62e9\u6587\u4ef6</p><p><span style=\" font-weight:700;\">Ctrl-V </span>\u7c98\u8d34\u526a\u5207\u677f\u56fe\u7247</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageLabel.setText("")
#if QT_CONFIG(tooltip)
        self.chooseButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.chooseButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.nameEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None))
#endif // QT_CONFIG(tooltip)
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None))
        self.pathLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\uff1a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u9884\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.imageTextEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.imageTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.saveButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u9884\u5904\u7406\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u7247", None))
#if QT_CONFIG(tooltip)
        self.saveNameEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None))
#endif // QT_CONFIG(tooltip)
        self.saveNameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
#if QT_CONFIG(tooltip)
        self.savePathLineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
        self.savePathLineEdit_2.setText("")
        self.savePathLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.getDirectoryButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.getDirectoryButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.cutButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u56fe\u7247\u88c1\u526a\u5668", None))
#endif // QT_CONFIG(tooltip)
        self.cutButton.setText(QCoreApplication.translate("MainWindow", u"\u88c1\u526a\u65cb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.resetButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u539f\u56fe", None))
#endif // QT_CONFIG(tooltip)
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u590d\u539f", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u56fe\u50cf\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.predictButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5f00\u59cb<span style=\" font-weight:700;\">AI</span>\u8bc6\u522b</p><p>(\u9996\u6b21\u8bc6\u522b\u53ef\u80fd\u82b1\u8d39\u8f83\u957f\u65f6\u95f4)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.predictButton.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
        self.resultLabel.setText("")
        self.label_3.setText("")
        self.resultLabel_2.setText("")
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5bfc\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u64cd\u4f5c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8def\u5f84", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u9884\u6d4b\u7ed3\u679c", None));
#if QT_CONFIG(whatsthis)
        self.tableWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.clearTableButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6e05\u7a7a", None))
#endif // QT_CONFIG(tooltip)
        self.clearTableButton.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u9884\u6d4b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
#if QT_CONFIG(tooltip)
        self.savePathLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u4fdd\u5b58\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.getDirectoryButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4fdd\u5b58\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
        self.getDirectoryButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.batchRenameRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u91cd\u547d\u540d", None))
#if QT_CONFIG(tooltip)
        self.batchExportButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ee5\u6587\u4ef6\u5939\u65b9\u5f0f\u6279\u91cf\u5bfc\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.batchExportButton.setText(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u7ed3\u679c\u5bfc\u51fa", None))
        self.batchPredictButton.setText(QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u6279\u91cf\u9884\u6d4b", None))
        self.batchImportLabel.setText("")
#if QT_CONFIG(tooltip)
        self.batchChooseButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.batchChooseButton.setText("")
#if QT_CONFIG(tooltip)
        self.statisticsTextEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u4fe1\u606f\u5c55\u793a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.statisticsButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u67f1\u72b6\u5806\u53e0\u56fe\u7edf\u8ba1\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u9884\u6d4b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.menu_M.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b(&M)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

