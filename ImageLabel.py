from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel


class ImageLabel(QLabel):

    pixmap_signal = Signal(bool, str, QPixmap)

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.setScaledContents(True)
        self.pixmap = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage() or event.mimeData().hasUrls():
            print(event.mimeData().hasImage())
            print(event.mimeData().hasUrls())
            event.acceptProposedAction()

    def dropEvent(self, event):
        tag = None
        url = None
        if event.mimeData().hasImage():
            url = event.mimeData().text()
            self.pixmap = QPixmap(event.mimeData().imageData())
            tag = True
        elif event.mimeData().hasUrls():
            text = event.mimeData().text()
            url = text.split("file:///")[-1]
            self.pixmap = QPixmap(url)
            tag = False
        print(url)
        self.pixmap_signal[bool, str, QPixmap].emit(tag, url, self.pixmap)
        event.acceptProposedAction()
