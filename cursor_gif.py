from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QApplication


class QCursorGif:

    def __init__(self, cursors, parent=None):
        # 记录默认的光标
        self._oldCursor = Qt.ArrowCursor
        self.setOldCursor(parent)
        # 加载光标图片
        self._cursorImages = [
            QCursor(QPixmap(cursor)) for cursor in cursors]
        self._cursorIndex = 0
        self._cursorCount = len(self._cursorImages) - 1
        # 创建刷新定时器
        self._cursorTimeout = 200
        self._cursorTimer = QTimer(parent)
        self._cursorTimer.timeout.connect(self._doBusy)

    def _doBusy(self):
        if self._cursorIndex > self._cursorCount:
            self._cursorIndex = 0
        QApplication.instance().setOverrideCursor(
            self._cursorImages[self._cursorIndex])
        self._cursorIndex += 1

    def startBusy(self):
        if not self._cursorTimer.isActive():
            self._cursorTimer.start(self._cursorTimeout)

    def stopBusy(self):
        self._cursorTimer.stop()
        QApplication.instance().setOverrideCursor(self._oldCursor)
        self.restore_cursor()

    @staticmethod
    def restore_cursor():
        while QApplication.instance().overrideCursor() is not None:
            QApplication.restoreOverrideCursor()

    def setCursorTimeout(self, timeout):
        self._cursorTimeout = timeout

    def setOldCursor(self, parent=None):
        self._oldCursor = (parent.cursor() or Qt.ArrowCursor) if parent else (
                QApplication.instance().overrideCursor() or Qt.ArrowCursor)
