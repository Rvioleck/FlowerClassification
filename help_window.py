import sys

from PySide6.QtCore import Qt, Signal, Property, QTimer
from PySide6.QtGui import QBitmap, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from ui_aboutWindow import Ui_AboutWindow
from ui_tutorialWindow import Ui_TutorialWindow

from PySide6.QtCore import Signal as pyqtSignal, Property as pyqtProperty, Qt, QPropertyAnimation, \
    QEasingCurve, QPointF
from PySide6.QtGui import QPainter, QTransform
from PySide6.QtWidgets import QWidget


class FlipWidget(QWidget):
    Left = 0  # 从右往左
    Right = 1  # 从左往右
    Scale = 3  # 图片缩放比例
    finished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(FlipWidget, self).__init__(*args, **kwargs)
        # 无边框无任务栏
        self.setWindowFlags(self.windowFlags() |
                            Qt.FramelessWindowHint | Qt.SubWindow)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 翻转角度
        self._angle = 0
        # 属性动画针对自定义属性`angle`
        self._animation = QPropertyAnimation(self, b'angle', self)
        self._animation.setDuration(550)
        self._animation.setEasingCurve(QEasingCurve.OutInQuad)
        self._animation.finished.connect(self.finished.emit)

    @Property(int)
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle
        self.update()

    def updateImages(self, direction, image1, image2):
        """设置两张切换图
        :param direction:        方向
        :param image1:           图片1
        :param image2:           图片2
        """
        self.image1 = image1
        self.image2 = image2
        self.show()
        self._angle = 0
        # 根据方向设置动画的初始和结束值
        if direction == self.Right:
            self._animation.setStartValue(1)
            self._animation.setEndValue(-180)
        elif direction == self.Left:
            self._animation.setStartValue(1)
            self._animation.setEndValue(180)
        self._animation.start()

    def paintEvent(self, event):
        super(FlipWidget, self).paintEvent(event)

        if hasattr(self, 'image1') and hasattr(self, 'image2') and self.isVisible():

            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

            # 变换
            transform = QTransform()
            # 把圆心设置为矩形中心
            transform.translate(self.width() / 2, self.height() / 2)

            if self._angle >= -90 and self._angle <= 90:
                # 当翻转角度在90范围内显示第一张图，且从大图缩放到小图的过程
                painter.save()
                # 设置翻转角度
                transform.rotate(self._angle, Qt.YAxis)
                painter.setTransform(transform)
                # 缩放图片高度
                width = self.image1.width() / 2
                height = int(self.image1.height() *
                             (1 - abs(self._angle / self.Scale) / 100))
                image = self.image1.scaled(
                    self.image1.width(), height,
                    Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                painter.drawPixmap(
                    QPointF(-width, -height / 2), image)
                painter.restore()
            else:
                # 当翻转角度在90范围内显示第二张图，且从小图缩放到原图的过程
                painter.save()
                if self._angle > 0:
                    angle = 180 + self._angle
                else:
                    angle = self._angle - 180
                # 设置翻转角度， 注意这里角度有差异
                transform.rotate(angle, Qt.YAxis)
                painter.setTransform(transform)
                # 缩放图片高度
                width = self.image2.width() / 2
                height = int(self.image2.height() *
                             (1 - ((360 - abs(angle)) / self.Scale / 100)))
                image = self.image2.scaled(
                    self.image2.width(), height,
                    Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                painter.drawPixmap(
                    QPointF(-width, -height / 2), image)
                painter.restore()



class AboutWindow(QMainWindow, Ui_AboutWindow):
    windowChanged = Signal()

    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.pix = QBitmap("images/mask.png")
        self.setMask(self.pix)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.emitSignal)

    def emitSignal(self):
        self.windowChanged[None].emit()


class TutorialWindow(QMainWindow, Ui_TutorialWindow):
    windowChanged = Signal()

    def __init__(self, parent=None):
        super(TutorialWindow, self).__init__(parent)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.pix = QBitmap("images/mask.png")
        self.setMask(self.pix)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.emitSignal)

    def emitSignal(self):
        self.windowChanged[None].emit()


class HelpWindow(QStackedWidget):
    # 主窗口

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPosition() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        elif event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_drag:
            # 当左键移动窗体修改偏移值
            self.move(event.globalPosition().toPoint() - self.m_DragPosition.toPoint())
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def __init__(self, *args, **kwargs):
        super(HelpWindow, self).__init__(*args, **kwargs)
        self.resize(428, 329)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # 这个是动画窗口，先创建不显示
        self.flipWidget = FlipWidget()
        self.flipWidget.finished.connect(self.showWidget)

        # 登录窗口
        self.aboutWindow = AboutWindow(self)
        self.aboutWindow.windowChanged[None].connect(self.jumpSettingWidget)
        self.addWidget(self.aboutWindow)

        # 设置窗口
        self.tutorialWindow = TutorialWindow(self)
        self.tutorialWindow.windowChanged[None].connect(self.jumpLoginWidget)
        self.addWidget(self.tutorialWindow)

    def showWidget(self):
        # 显示主窗口隐藏动画窗口
        self.setWindowOpacity(1)
        QTimer.singleShot(100, self.flipWidget.hide)

    def jumpLoginWidget(self):
        # 翻转到登录界面
        self.setWindowOpacity(0)  # 类似隐藏，但是保留了任务栏
        self.setCurrentWidget(self.aboutWindow)  # 很重要，一定要先切换过去，不然会导致第一次截图有误
        image1 = self.aboutWindow.grab()  # 截图1
        image2 = self.tutorialWindow.grab()  # 截图2
        padding = 100  # 扩大边距 @UnusedVariable
        self.flipWidget.setGeometry(self.geometry())
        # .adjusted(-padding, -padding, padding, padding))
        self.flipWidget.updateImages(FlipWidget.Right, image2, image1)

    def jumpSettingWidget(self):
        # 翻转到设置界面
        self.setWindowOpacity(0)  # 类似隐藏，但是保留了任务栏
        self.setCurrentWidget(self.tutorialWindow)  # 很重要，一定要先切换过去，不然会导致第一次截图有误
        image1 = self.aboutWindow.grab()  # 截图1
        image2 = self.tutorialWindow.grab()  # 截图2
        padding = 100  # 扩大边距 @UnusedVariable
        self.flipWidget.setGeometry(self.geometry())
        # .adjusted(-padding, -padding, padding, padding))
        self.flipWidget.updateImages(FlipWidget.Left, image1, image2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = HelpWindow()
    myMainWindow.show()
    sys.exit(app.exec())
