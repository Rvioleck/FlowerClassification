from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect


class ImageLabel(QLabel):
    pixmap_signal = Signal(bool, str, QPixmap)

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.setScaledContents(True)
        self.my_pixmap = None
        self.effect_shadow = QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(8, 8)  # 偏移
        self.effect_shadow.setBlurRadius(15)  # 阴影半径
        self.effect_shadow.setColor(Qt.gray)
        self.setGraphicsEffect(self.effect_shadow)

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
            self.my_pixmap = QPixmap(event.mimeData().imageData())
            tag = True
        elif event.mimeData().hasUrls():
            text = event.mimeData().text()
            url = text.split("file:///")[-1]
            self.my_pixmap = QPixmap(url)
            tag = False
        print(url)
        self.pixmap_signal[bool, str, QPixmap].emit(tag, url, self.my_pixmap)
        event.acceptProposedAction()
