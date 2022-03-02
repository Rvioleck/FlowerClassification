import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QLineEdit, QInputDialog, QFileDialog, \
    QColorDialog, QFontDialog, QLabel, QPushButton, QVBoxLayout, QStyle
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPen, QColor, QBrush, QFont, QAction
from PySide6.QtCore import Qt, QRect


class mylable(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    def __init__(self, parent):
        super(mylable, self).__init__(parent)
        self.pixmap = QPixmap(597, 497)  # 考虑边框的间距 减去px
        self.pixmap.fill(Qt.white)
        self.setStyleSheet("border: 2px solid red")
        self.Color = Qt.blue  # pen color: defult:blue
        self.penwidth = 4  # pen width : default:4

    def paintEvent(self, event):
        # super().paintEvent(event)

        painter = QPainter(self.pixmap)
        painter.setPen(QPen(self.Color, self.penwidth, Qt.SolidLine))
        painter.drawLine(self.x0, self.y0, self.x1, self.y1)

        Label_painter = QPainter(self)
        Label_painter.drawPixmap(2, 2, self.pixmap)

    def mousePressEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()
        self.flag = True

    def mouseMoveEvent(self, event):
        if self.flag:
            self.x0 = self.x1
            self.y0 = self.y1
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        self.flag = False


class cb(QMainWindow):
    def __init__(self):
        super(cb, self).__init__()
        self.initUi()

    def initUi(self):
        self.resize(800, 600)
        vbox = QVBoxLayout()
        # 选择绘画文件 按钮
        self.button_file = QPushButton(self)
        self.button_file.setGeometry(660, 80, 100, 50)
        self.button_file.setText("File")
        self.button_file.setFont(QFont("Chiller", 20))
        vbox.addWidget(self.button_file)
        vbox.addStretch()
        # 选择画笔颜色 按钮
        self.button_color = QPushButton(self)
        self.button_color.setGeometry(660, 270, 100, 50)
        self.button_color.setText("Color")
        self.button_color.setFont(QFont("Chiller", 20))
        vbox.addWidget(self.button_color)
        vbox.addStretch()
        # 选择画笔粗细 按钮
        self.button_width = QPushButton(self)
        self.button_width.setGeometry(660, 460, 100, 50)
        self.button_width.setText("Width")
        self.button_width.setFont(QFont("Chiller", 20))
        vbox.addWidget(self.button_width)
        vbox.addStretch()
        # 设置画板
        self.lb = mylable(self)
        self.lb.setGeometry(20, 40, 601, 501)
        # 橡皮
        eraser = QAction(QIcon("1239616.png"), "Eraser", self)
        eraser.setToolTip("Eraser")
        # 工具栏
        self.menubar = self.addToolBar("ToolBar")
        self.menubar.addAction(eraser)
        # 主页面
        self.setWindowIcon(QIcon("1216867.png"))
        self.setWindowTitle("Drawing Board")

        self.button_file.clicked.connect(self.openfile)
        self.button_color.clicked.connect(self.choose_color)
        eraser.triggered.connect(self.erase)
        self.button_width.clicked.connect(self.choose_width)

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, "选择图片文件", ".")
        if fname[0]:
            self.lb.pixmap = QPixmap(fname[0])

    def choose_color(self):
        Color = QColorDialog.getColor()  # color是Qcolor
        if Color.isValid():
            self.lb.Color = Color

    def erase(self):
        self.lb.Color = Qt.white
        self.lb.setCursor(Qt.CrossCursor)
        self.lb.penwidth = self.lb.penwidth + 2

    def choose_width(self):
        width, ok = QInputDialog.getInt(self, '选择画笔粗细', '请输入粗细：', min=1, step=1)
        if ok:
            self.lb.penwidth = width


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = cb()
    mainwindow.show()
    sys.exit(app.exec_())
