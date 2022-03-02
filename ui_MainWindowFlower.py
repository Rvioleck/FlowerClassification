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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
                               QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
                               QToolButton, QVBoxLayout, QWidget)
import apprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/pic/images/python.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.myModelAction = QAction(MainWindow)
        self.myModelAction.setObjectName(u"myModelAction")
        self.denseNet121Action = QAction(MainWindow)
        self.denseNet121Action.setObjectName(u"denseNet121Action")
        self.alexNetAction = QAction(MainWindow)
        self.alexNetAction.setObjectName(u"alexNetAction")
        self.vggAction = QAction(MainWindow)
        self.vggAction.setObjectName(u"vggAction")
        self.inceptionAction = QAction(MainWindow)
        self.inceptionAction.setObjectName(u"inceptionAction")
        self.resNetAction = QAction(MainWindow)
        self.resNetAction.setObjectName(u"resNetAction")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon1 = QIcon()
        icon1.addFile(u"images/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon1)
        font = QFont()
        font.setPointSize(10)
        self.actionNew.setFont(font)
        self.actionNew.setShortcutContext(Qt.WidgetWithChildrenShortcut)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon2 = QIcon()
        icon2.addFile(u"images/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setFont(font)
        self.actionOpen.setShortcutContext(Qt.WidgetWithChildrenShortcut)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon3 = QIcon()
        icon3.addFile(u"images/close.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setFont(font)
        self.actionCNN = QAction(MainWindow)
        self.actionCNN.setObjectName(u"actionCNN")
        icon4 = QIcon()
        iconThemeName = u"\u7edf\u8ba1"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"images/\u6298\u7ebf\u56fe\u5206\u5e03.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionCNN.setIcon(icon4)
        self.mobileNetAction = QAction(MainWindow)
        self.mobileNetAction.setObjectName(u"mobileNetAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 901, 531))
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 13, 331, 331))
        self.imageLabel = QLabel(self.groupBox)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(50, 97, 224, 224))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(224, 224))
        self.imageLabel.setMaximumSize(QSize(224, 224))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.imageLabel.setFont(font1)
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setPixmap(QPixmap(u"images/\u56fe\u7247\u6dfb\u52a0.png"))
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
        icon5 = QIcon()
        icon5.addFile(u":/pic/images/\u6253\u5f00\u56fe\u7247.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chooseButton.setIcon(icon5)
        self.chooseButton.setIconSize(QSize(32, 32))
        self.chooseButton.setAutoDefault(False)
        self.chooseButton.setFlat(True)
        self.nameEdit = QLineEdit(self.groupBox)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(50, 64, 261, 21))
        self.nameEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.nameEdit.setReadOnly(True)
        self.pathLabel = QLabel(self.groupBox)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setGeometry(QRect(50, 20, 261, 41))
        sizePolicy.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy)
        self.pathLabel.setMinimumSize(QSize(0, 30))
        self.pathLabel.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        self.pathLabel.setFont(font2)
        self.pathLabel.setTextFormat(Qt.RichText)
        self.pathLabel.setAlignment(Qt.AlignCenter)
        self.pathLabel.setWordWrap(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 31, 16))
        self.groupBox_4 = QGroupBox(self.tab1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 355, 331, 141))
        self.cutButton = QPushButton(self.groupBox_4)
        self.cutButton.setObjectName(u"cutButton")
        self.cutButton.setGeometry(QRect(230, 20, 91, 31))
        self.cutButton.setStyleSheet(u"QPushButton\n"
                                     "                  {\n"
                                     "                    background-color:transparent;\n"
                                     "                    border:2px solid #0782f5;\n"
                                     "                    border-radius:5px;\n"
                                     "                    color:black\n"
                                     "                  }\n"
                                     "                  QPushButton:hover\n"
                                     "                  {\n"
                                     "                    background-color:rgb(255, 248, 250);\n"
                                     "                    border:2px solid #5F92B2;\n"
                                     "                    border-radius:5px;\n"
                                     "                    color:black;\n"
                                     "                  }\n"
                                     "                  QPushButton:hover:pressed\n"
                                     "                  {\n"
                                     "                    border:2px solid #5F92B2;\n"
                                     "                    border-radius:5px;\n"
                                     "                    color:black;\n"
                                     "					padding-right:3px;\n"
                                     "					padding-top:3px;\n"
                                     "                  }\n"
                                     "")
        icon6 = QIcon()
        icon6.addFile(u"images/\u622a\u53d6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cutButton.setIcon(icon6)
        self.cutButton.setIconSize(QSize(24, 24))
        self.imageTextEdit = QTextEdit(self.groupBox_4)
        self.imageTextEdit.setObjectName(u"imageTextEdit")
        self.imageTextEdit.setGeometry(QRect(10, 20, 211, 111))
        self.imageTextEdit.setReadOnly(True)
        self.resetButton = QPushButton(self.groupBox_4)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(230, 60, 91, 31))
        self.resetButton.setStyleSheet(u"QPushButton\n"
                                       "                  {\n"
                                       "                    background-color:transparent;\n"
                                       "                    border:2px solid #0782f5;\n"
                                       "                    border-radius:5px;\n"
                                       "                    color:black\n"
                                       "                  }\n"
                                       "                  QPushButton:hover\n"
                                       "                  {\n"
                                       "                    background-color:rgb(255, 248, 250);\n"
                                       "                    border:2px solid #5F92B2;\n"
                                       "                    border-radius:5px;\n"
                                       "                    color:black;\n"
                                       "                  }\n"
                                       "                  QPushButton:hover:pressed\n"
                                       "                  {\n"
                                       "                    border:2px solid #5F92B2;\n"
                                       "                    border-radius:5px;\n"
                                       "                    color:black;\n"
                                       "					padding-right:3px;\n"
                                       "					padding-top:3px;\n"
                                       "                  }\n"
                                       "")
        icon7 = QIcon()
        icon7.addFile(u"images/\u590d\u4f4d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon7)
        self.resetButton.setIconSize(QSize(21, 21))
        self.saveButton = QPushButton(self.groupBox_4)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(230, 100, 91, 31))
        self.saveButton.setStyleSheet(u"QPushButton\n"
                                      "                  {\n"
                                      "                    background-color:transparent;\n"
                                      "                    border:2px solid #0782f5;\n"
                                      "                    border-radius:5px;\n"
                                      "                    color:black\n"
                                      "                  }\n"
                                      "                  QPushButton:hover\n"
                                      "                  {\n"
                                      "                    background-color:rgb(255, 248, 250);\n"
                                      "                    border:2px solid #5F92B2;\n"
                                      "                    border-radius:5px;\n"
                                      "                    color:black;\n"
                                      "                  }\n"
                                      "                  QPushButton:hover:pressed\n"
                                      "                  {\n"
                                      "                    border:2px solid #5F92B2;\n"
                                      "                    border-radius:5px;\n"
                                      "                    color:black;\n"
                                      "					padding-right:3px;\n"
                                      "					padding-top:3px;\n"
                                      "                  }\n"
                                      "")
        icon8 = QIcon()
        icon8.addFile(u"images/\u4fdd\u5b58.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon8)
        self.saveButton.setIconSize(QSize(20, 20))
        self.groupBox_5 = QGroupBox(self.tab1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(380, 10, 491, 481))
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.predictButton = QPushButton(self.groupBox_5)
        self.predictButton.setObjectName(u"predictButton")
        self.predictButton.setGeometry(QRect(30, 30, 60, 25))
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
                                         "                  {\n"
                                         "                    background-color:transparent;\n"
                                         "                    border:2px solid #0782f5;\n"
                                         "                    border-radius:5px;\n"
                                         "                    color:black\n"
                                         "                  }\n"
                                         "QPushButton:hover\n"
                                         "{\n"
                                         "    /*\u80cc\u666f\u989c\u8272*/  \n"
                                         "    background-color:rgb(170, 200, 255);\n"
                                         "    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
                                         "}\n"
                                         "                  QPushButton:hover:pressed\n"
                                         "                  {\n"
                                         "                    border:2px solid #5F92B2;\n"
                                         "                    border-radius:5px;\n"
                                         "                    color:black;\n"
                                         "					padding-right:3px;\n"
                                         "					padding-top:3px;\n"
                                         "                  }\n"
                                         "")
        icon9 = QIcon()
        icon9.addFile(u"images/AI\u8bc6\u522b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.predictButton.setIcon(icon9)
        self.predictButton.setIconSize(QSize(24, 24))
        self.predictButton.setFlat(True)
        self.resultLabel = QLabel(self.groupBox_5)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(100, 30, 371, 25))
        sizePolicy.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy)
        self.resultLabel.setMinimumSize(QSize(0, 25))
        self.resultLabel.setMaximumSize(QSize(16777215, 25))
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.groupBox_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 60, 451, 401))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tableWidget = QTableWidget(self.tab2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        icon10 = QIcon()
        icon10.addFile(u"images/\u6587\u4ef6\u5939 (2).png", QSize(), QIcon.Normal, QIcon.Off)
        font3 = QFont()
        font3.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font3.setPointSize(11)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setIcon(icon10);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon11 = QIcon()
        icon11.addFile(u"images/\u56fe\u7247(1).png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setIcon(icon11);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon12 = QIcon()
        icon12.addFile(u"images/\u82b1\u6735.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setIcon(icon12);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 431, 471))
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setIconSize(QSize(24, 24))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.clearTableButton = QPushButton(self.tab2)
        self.clearTableButton.setObjectName(u"clearTableButton")
        self.clearTableButton.setGeometry(QRect(400, 470, 35, 35))
        sizePolicy1.setHeightForWidth(self.clearTableButton.sizePolicy().hasHeightForWidth())
        self.clearTableButton.setSizePolicy(sizePolicy1)
        self.clearTableButton.setMinimumSize(QSize(35, 35))
        self.clearTableButton.setMaximumSize(QSize(35, 35))
        self.clearTableButton.setLayoutDirection(Qt.LeftToRight)
        self.clearTableButton.setAutoFillBackground(False)
        self.clearTableButton.setStyleSheet(u"QPushButton:hover\n"
                                            "{\n"
                                            "	background-color: rgb(224, 255, 254);\n"
                                            "	border:2px solid #5F92B2;\n"
                                            "	border-radius:5px;\n"
                                            "	color:white;\n"
                                            "}")
        icon13 = QIcon()
        icon13.addFile(u"images/\u5220\u9664.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearTableButton.setIcon(icon13)
        self.clearTableButton.setIconSize(QSize(24, 24))
        self.clearTableButton.setFlat(True)
        self.groupBox_2 = QGroupBox(self.tab2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(450, 130, 421, 111))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 33, 401, 67))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.savePathLineEdit = QLineEdit(self.layoutWidget)
        self.savePathLineEdit.setObjectName(u"savePathLineEdit")

        self.horizontalLayout.addWidget(self.savePathLineEdit)

        self.getDirectoryButton = QToolButton(self.layoutWidget)
        self.getDirectoryButton.setObjectName(u"getDirectoryButton")
        icon14 = QIcon()
        icon14.addFile(u"images/\u6587\u4ef6\u5939.png", QSize(), QIcon.Normal, QIcon.Off)
        self.getDirectoryButton.setIcon(icon14)
        self.getDirectoryButton.setIconSize(QSize(24, 24))
        self.getDirectoryButton.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.getDirectoryButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.batchRenameRadioButton = QRadioButton(self.layoutWidget)
        self.batchRenameRadioButton.setObjectName(u"batchRenameRadioButton")

        self.horizontalLayout_2.addWidget(self.batchRenameRadioButton)

        self.batchExportButton = QPushButton(self.layoutWidget)
        self.batchExportButton.setObjectName(u"batchExportButton")
        sizePolicy2.setHeightForWidth(self.batchExportButton.sizePolicy().hasHeightForWidth())
        self.batchExportButton.setSizePolicy(sizePolicy2)
        self.batchExportButton.setMinimumSize(QSize(80, 25))
        self.batchExportButton.setMaximumSize(QSize(80, 25))
        self.batchExportButton.setLayoutDirection(Qt.LeftToRight)
        self.batchExportButton.setAutoFillBackground(False)
        self.batchExportButton.setStyleSheet(u"QPushButton\n"
                                             "                  {\n"
                                             "                    background-color:rgb(134,183,200);\n"
                                             "                    border:2px solid #5F92B2;\n"
                                             "                    border-radius:5px;\n"
                                             "                    color:white\n"
"                  }\n"
"                  QPushButton:hover\n"
"                  {\n"
"                    background-color:rgb(0,130,150);\n"
"                    border:2px solid #5F92B2;\n"
"                    border-radius:5px;\n"
"                    color:white;\n"
"                  }\n"
"                  QPushButton:hover:pressed\n"
"                  {\n"
"                    background-color:rgb(85,170,255); \n"
"                    border:2px solid #3C80B1;\n"
"                    border-radius:5px;\n"
"                    color:white;\n"
"                  }\n"
"")
        self.batchExportButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.batchExportButton)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox_3 = QGroupBox(self.tab2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(450, 10, 171, 111))
        self.batchChooseButton = QPushButton(self.groupBox_3)
        self.batchChooseButton.setObjectName(u"batchChooseButton")
        self.batchChooseButton.setGeometry(QRect(10, 20, 40, 40))
        sizePolicy2.setHeightForWidth(self.batchChooseButton.sizePolicy().hasHeightForWidth())
        self.batchChooseButton.setSizePolicy(sizePolicy2)
        self.batchChooseButton.setMinimumSize(QSize(40, 40))
        self.batchChooseButton.setMaximumSize(QSize(40, 40))
        self.batchChooseButton.setLayoutDirection(Qt.LeftToRight)
        icon15 = QIcon()
        icon15.addFile(u"images/\u5bfc\u5165.png", QSize(), QIcon.Normal, QIcon.Off)
        self.batchChooseButton.setIcon(icon15)
        self.batchChooseButton.setIconSize(QSize(24, 24))
        self.batchChooseButton.setFlat(True)
        self.batchPredictButton = QPushButton(self.groupBox_3)
        self.batchPredictButton.setObjectName(u"batchPredictButton")
        self.batchPredictButton.setGeometry(QRect(20, 70, 80, 25))
        sizePolicy2.setHeightForWidth(self.batchPredictButton.sizePolicy().hasHeightForWidth())
        self.batchPredictButton.setSizePolicy(sizePolicy2)
        self.batchPredictButton.setMinimumSize(QSize(80, 25))
        self.batchPredictButton.setMaximumSize(QSize(80, 25))
        self.batchPredictButton.setLayoutDirection(Qt.LeftToRight)
        self.batchPredictButton.setAutoFillBackground(False)
        self.batchPredictButton.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
                                              "QPushButton\n"
                                              "{\n"
                                              "    /*\u5b57\u4f53\u4e3a\u5fae\u8f6f\u96c5\u9ed1*/\n"
                                              "    font-family:Microsoft Yahei;\n"
                                              "    /*\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272*/    \n"
                                              "    color:white;\n"
                                              "    /*\u80cc\u666f\u989c\u8272*/  \n"
                                              "    background-color:rgb(14 , 150 , 254);\n"
                                              "    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a8\u50cf\u7d20*/ \n"
                                              "    border-radius:8px;\n"
                                              "}\n"
                                              " \n"
                                              "/*\u6309\u94ae\u505c\u7559\u6001*/\n"
                                              "QPushButton:hover\n"
                                              "{\n"
                                              "    /*\u80cc\u666f\u989c\u8272*/  \n"
                                              "    background-color:rgb(170, 200, 255);\n"
                                              "    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
                                              "    padding-right:3px;\n"
                                              "    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
                                              "	padding-bottom:3px;\n"
                                              "	color:rgb(255, 255, 255);\n"
                                              "}\n"
                                              " \n"
                                              "/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
                                              "QPushButton:pressed\n"
                                              "{\n"
                                              "    /*\u80cc\u666f\u989c"
                                              "\u8272*/  \n"
                                              "    background-color:rgb(14 , 135 , 255);\n"
                                              "    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
                                              "    padding-left:3px;\n"
                                              "    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
                                              "	padding-top:3px;\n"
                                              "}")
        self.batchPredictButton.setFlat(False)
        self.batchImportLabel = QLabel(self.tab2)
        self.batchImportLabel.setObjectName(u"batchImportLabel")
        self.batchImportLabel.setGeometry(QRect(9, 477, 391, 21))
        font4 = QFont()
        font4.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font4.setPointSize(11)
        self.batchImportLabel.setFont(font4)
        self.tabWidget.addTab(self.tab2, "")
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.tableWidget.raise_()
        self.clearTableButton.raise_()
        self.batchImportLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setToolTipsVisible(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.toolBar.addAction(self.myModelAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.denseNet121Action)
        self.toolBar.addAction(self.mobileNetAction)
        self.toolBar.addAction(self.inceptionAction)
        self.toolBar.addAction(self.alexNetAction)
        self.toolBar.addAction(self.resNetAction)
        self.toolBar.addAction(self.vggAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCNN)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.chooseButton.setDefault(False)


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
        self.denseNet121Action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.alexNetAction.setText(QCoreApplication.translate("MainWindow", u"AlexNet8", None))
        # if QT_CONFIG(shortcut)
        self.alexNetAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
        # endif // QT_CONFIG(shortcut)
        self.vggAction.setText(QCoreApplication.translate("MainWindow", u"VGG19", None))
        # if QT_CONFIG(tooltip)
        self.vggAction.setToolTip(QCoreApplication.translate("MainWindow", u"VGG19", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.vggAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
        # endif // QT_CONFIG(shortcut)
        self.inceptionAction.setText(QCoreApplication.translate("MainWindow", u"InceptionV3", None))
        # if QT_CONFIG(tooltip)
        self.inceptionAction.setToolTip(QCoreApplication.translate("MainWindow", u"InceptionV3", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.inceptionAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
        # endif // QT_CONFIG(shortcut)
        self.resNetAction.setText(QCoreApplication.translate("MainWindow", u"ResNet50", None))
        # if QT_CONFIG(tooltip)
        self.resNetAction.setToolTip(QCoreApplication.translate("MainWindow", u"ResNet50", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.resNetAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
        # endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa(&N)", None))
        # if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
        # endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(&O)", None))
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
        # endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed(&C)", None))
        self.actionCNN.setText(QCoreApplication.translate("MainWindow", u"CNN\u6a21\u578b\u7edf\u8ba1", None))
        self.mobileNetAction.setText(QCoreApplication.translate("MainWindow", u"MobileNetV2", None))
        # if QT_CONFIG(tooltip)
        self.mobileNetAction.setToolTip(QCoreApplication.translate("MainWindow", u"MobileNetV2", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.mobileNetAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
        # endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u5165", None))
        # if QT_CONFIG(tooltip)
        self.imageLabel.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u53cc\u51fb\u9009\u62e9\u6587\u4ef6", None))
        # endif // QT_CONFIG(tooltip)
        self.imageLabel.setText("")
        self.chooseButton.setText("")
        # if QT_CONFIG(shortcut)
        self.chooseButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
        # endif // QT_CONFIG(shortcut)
        self.nameEdit.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None))
        self.pathLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\uff1a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u9884\u5904\u7406", None))
        self.cutButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u88c1\u526a", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d\u539f\u56fe", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.groupBox_5.setTitle(
            QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u56fe\u50cf\u8bc6\u522b", None))
        self.predictButton.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
        self.resultLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1),
                                  QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u64cd\u4f5c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8def\u5f84", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u9884\u6d4b\u7ed3\u679c", None));
        # if QT_CONFIG(whatsthis)
        self.tableWidget.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.clearTableButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6e05\u7a7a", None))
        # endif // QT_CONFIG(tooltip)
        self.clearTableButton.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u5bfc\u51fa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.getDirectoryButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.batchRenameRadioButton.setText(
            QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u91cd\u547d\u540d", None))
        self.batchExportButton.setText(
            QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u7ed3\u679c\u5bfc\u51fa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u5165", None))
        # if QT_CONFIG(tooltip)
        self.batchChooseButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165\u56fe\u7247", None))
        # endif // QT_CONFIG(tooltip)
        self.batchChooseButton.setText("")
        self.batchPredictButton.setText(
            QCoreApplication.translate("MainWindow", u"\u82b1\u6735\u6279\u91cf\u9884\u6d4b", None))
        self.batchImportLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2),
                                  QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u9884\u6d4b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

