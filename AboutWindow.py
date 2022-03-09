import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QBitmap, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_aboutWindow import Ui_AboutWindow


class AboutWindow(QMainWindow, Ui_AboutWindow):

    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.pix = QBitmap("images/mask.png")
        self.setMask(self.pix)
        self.setupUi(self)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = AboutWindow()
    myMainWindow.show()
    sys.exit(app.exec())
