# -*- coding: utf-8 -*-

import base64
import sys

from PySide6.QtCore import Qt, QRectF, QSize, Signal, QTimer
from PySide6.QtGui import QPixmap, QImage, QPainter, QPainterPath, \
    QColor, QCursor
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, \
    QGridLayout, QSpacerItem, QSizePolicy, QGraphicsDropShadowEffect, \
    QListWidget, QListWidgetItem, QApplication, QPushButton


class NotificationIcon:
    Info, Success, Warning, Error, Close = range(5)
    Types = {
        Info: None,
        Success: None,
        Warning: None,
        Error: None,
        Close: None
    }

    @classmethod
    def init(cls):
        cls.Types[cls.Info] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC5ElEQVRYR8VX0VHbQBB9e/bkN3QQU0FMBSEVYFcQ8xPBJLJ1FWAqOMcaxogfTAWQCiAVRKkgTgfmM4zRZu6QhGzL0p0nDPr17e7bt7tv14RX/uiV48MJgAon+8TiAMRtMFogaqUJxADPwRRzg67kl8+xbWJWANR40iPQSSFgtX/mGQkaDr56V3VAKgGos4s2JXwJoF3naMPvMS+SrpTHs032GwGkdF+DsFMVnJm/oyGGeHico0EjIjpYes+YMyVd6R/flfkpBWCCQ9zaZM2LZDfLMGXsZ5kdI/lYBmINgHHyyLd1mWdBbAFAM/GY7K2WYx1AeB4T6L1N9umbGxZ0qktATaEAdCps48D39oq/LwEw3U5CN92LfczJoewfT7MAywDCaEbAuxeLrh0zz4L+0e4aAJfGy+sP3IMxlH1vpMJoSMCJDXgWtJeJVc6ACs9HBBrYODCJAFdYvAmkPJxnNqMwYht7Bn+T/lGg3z4DGEd3RPhQ54DBvwAOVkeqagRXfTLjh+x7+8sALOtfHLuiYzWOAiLoKbD58mnIGbCmLxUepS6NQmYlUGE0JeCTTXT9JvA9E9sZgO5iIpoyc6/YzcqSwQzgGgBXB7oXpH9klpRSkxY1xW/b7Iu2zk34PILPnazCqEPAtTWA8iZ0HsOu9L0bw4DzCJeNocMGNDpQ3IKO+6NUiJ4ysZNiBv5I3zPnmJmG5oM+wbS+9+qkvGi7NAXGmeUy0ioofa+XA0jH0UaMKpdRWs/adcwMqfV/tenqpqHY/Znt+j2gJi00RUzA201dXaxh9iZdZloJS+9H1otrkbRrD5InFqpPskxEshJQ468CkSmJC+i1HigaaxCAuCljgoDhwPdOjf7rFVxxuJrMkXScjtKc1rOLNpJk6nii5XmYzbngzlZn+RIb40kPJPTBYXUt6VEDJ8Pi6bWpNFb/jFYY6YGpDeKdjBmTKdMcxDGEmP73v2a2Gr/NOycGtglQZ/MPzEqCMLGckJEAAAAASUVORK5CYII=')))
        cls.Types[cls.Success] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACZUlEQVRYR8VXS3LTQBDtVsDbcAPMCbB3limkcAKSG4QFdnaYE2BOQLKzxSLJCeAGSUQheSnfwLmB2VJhXmpExpFHI2sk2RWv5FJPv9evP9NieuIfPzE+VSJw8qt3IMDvmahDoDYxt2UAACXMWIIowR5ffn8TJbaBWRE4CXvHAH9RgKXOgQUI48CfXZbZbiTw8Xe/w3d0zkydMkem91IZpyWOJu5sUXS+kEAqt3B+MNOLOuDqDEBLxxFHk7eza5MfIwEJDjhXTYD1s8zinYlEjsCD7FdNI9cJpEq0RFdPR47AMOzLCn69zegz6UgCP+pmfa8RSKudnPNdgCufTOLDxJtdPP7PoA1Cd8HEL5sSUCCD0B0x8bc1f8Bi6sevcgS2VXh6hMOwDz0gsUddNaxWKRjeuKfE/KlJ9Dq4UYH/o/Ns6scj+bgiMAjdayb26xLQwTfVEwg3gRcf6ARq578KuLo7VDc8psCQqwfjr4EfjYvkrAquFJ56UYpdSkAZSmNd1rrg0leOQFELgvA58OJTxVyRaAJORPOpF6UXnFUR5sDiXjs7UqsOMGMRlrWhTkJXpFL3mNrQZhA1lH3F0TiI5FurUQyMpn58VjhkSqQA4Tbw4nSVW6sBU5VXktXSeONlJH3s8jrOVr9RgVSFuNcWfzlh5n3LoKzMAPxxWuiULiQpiR2sZNnCyzIuWUr5Z1Ml0sgdHFZaShVDuR86/0huL3VXtDk/F4e11vKsTHLSCeKx7bYkW80hjLOrV1GhWH0ZrSlyh2MwdZhYfi8oZeYgLBmUiGd8sfVPM6syr2lUSYGaGBuP3QN6rVUwYV/egwAAAABJRU5ErkJggg==')))
        cls.Types[cls.Warning] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACmElEQVRYR8VXTW7TUBD+xjYSXZFukOIsSE9AskNJJMoJmq4r7OYEwAkabhBOkB/Emt4gVIojdpgbpIumEitX6gKB7UHPkauXxLHfc4F6Z3l+vvnmm/fGhAd+6IHzQwvA9cfOITMfAdQAcx1EdVEAM/tEFADsWyaPn57MfdXClABcT1qnzHSWJiwMzrwgoF91vXGRbS6AH59ajd8hDYmoURQo67tgxoij42rv62KX/04Agu44xmciVMokT32YERgGjquvZ1+y4mQCWPUa0/sk3vQlwqssEFsAVrQbU4XKL/ai2+5PPK6waQ4AOsoDnDARh83NdmwBuJq0fQI9L6p+L7rd3+/5gbAToMPI+FbkIzRRc72mbLcGIFE7jGFRIPHddmZrvstJh1X8CHGv6sxHqe1GkPYCoGcqgcoCAPPCdr2DLQC6wqMoPEj7qdqCNKllxs30sLpjYDluDUDGG5XqhY2sal3w4PiD7c7fJnHShMtJR8zpy/8CALiwndnhBgD1/t+XAXkaZAaUVHwnHulg0W6BNEWlAQD8zna8gQB0Ne70iXCm2j55jCUAei1gxvuaO+uXAcDg7zXHSy640iKUAehOEDJFqDmGQkiPLO5Fv+KADXOqvCuIsrPGsIyQdHou22YeRMJgOdHTQTkAfGk7XrLKrWlAvOhcRgBfWiZ3RQti0zxXuUFXCXMuo0TRitfxugjbIxC5RYzI6s9kIGFh+KLOpiW22id5AUuI8IaisFG4kCQg/sFKJgtPLix3KWXGeRETRbQDuCFCV2spTYMm+2FEI1WBbYIRPTeiqFtqLZeDraaD+qrbkpgQAvfl1WsXU0p/RjIjYYhTkNFgcCVlRlRKoAAc+5aF0V//NVPoc2kTLQZKZ8lx/AMXBmMwuXUwOAAAAABJRU5ErkJggg==')))
        cls.Types[cls.Error] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACrklEQVRYR82XW27aQBSG/4PtiNhIpStouoImKwjZAV1B07coWCpZQcgK6kh2lLeSFZSsIOwgdAdkBaUSEBQDpxpjU9vM+EJR03nDzJz/mzm3GcIrD3plfZQCeD47O1ho2jERNRmoE9AQG2BgBGBAwIiZe5Zh3JPjiG+5oxCAEF5q2iWITnMtRhOYu5XF4mr/9naYtSYXYGLbHQCXhYVTEwlom657rVqvBOB2uz71/a+ldq1SYe6ahnEhc4sSYGzbfQKOt915eh0D/ZrrnqS/SwEmrVYXRJ92Jb4OC+C65rrtuN0NgIltNwF837V4zN5Hy3V70e9NgFZrCKJ3CQDmJ9MwDsW36XzeB/AhA/CHqeuN2WxWX2paX2JraHneeynA+Pz8lCqVbxLjV5brimxAEJxqiEA8CjZVBvFy+bl2c9MV9hInoAw85qFpGEeRYQVEQjzMokcQHWxsiPne8jzh6j8AodGfyqNlHpiGcaKAkIk/gChwm2yYuv5W2FqfwLNtN5bAQ2bwySB83zENo50A8/1McaFRAU72XVek+mpk+D/JlIKI/xkee654uCbIhjVAqZIrgSgpLhiCwN4OAEj4vEB2yDybBCjsAol4ZD0nRdMQSRcUCsKUeNSw4o2mKMRGEOamoVx8FXDZKVosDYNMUHXAsBRnppo8RQcbpTgIGEkhykpFjnWxzGhPQYxt2yHgS/oIlKVYTJxImpG482nz+VG1Wh1N84pMCCGa0ULXHwmoJwCYnyzPW5fn/68dh7EgPbrMMl3gz7gro+n/7EoWD7w4a96l1NnJ1Yz5Lt6wCgFEk0r1CIkbiPnC9DxH5aHcd4FYGD5MOqVOg/muslh0/vphkm63k5eXZvA0I6qD+ZCI3jDzLxANiHn1NNvb6+30aVYgwLeeUsgFW1svsPA3Ncq4MHzVeO8AAAAASUVORK5CYII=')))
        cls.Types[cls.Close] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAeElEQVQ4T2NkoBAwUqifgboGzJy76AIjE3NCWmL0BWwumzV/qcH/f38XpCfHGcDkUVwAUsDw9+8GBmbmAHRDcMlheAGbQnwGYw0DZA1gp+JwFUgKZyDCDQGpwuIlrGGAHHAUGUCRFygKRIqjkeKERE6+oG5eIMcFAOqSchGwiKKAAAAAAElFTkSuQmCC')))

    @classmethod
    def icon(cls, ntype):
        return cls.Types.get(ntype)


class NotificationItem(QWidget):
    closed = Signal(QListWidgetItem)

    def __init__(self, title, message, item, *args, ntype=0, callback=None, time=5000, **kwargs):
        super(NotificationItem, self).__init__(*args, **kwargs)
        self.item = item
        self.callback = callback
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.bgWidget = QWidget(self)  # ????????????, ????????????????????????
        layout.addWidget(self.bgWidget)
        layout = QGridLayout(self.bgWidget)
        layout.setHorizontalSpacing(15)

        # ??????????????????
        layout.addWidget(
            QLabel(self, pixmap=NotificationIcon.icon(ntype)), 0, 0)

        # ??????
        self.labelTitle = QLabel(title, self)
        font = self.labelTitle.font()
        font.setBold(True)
        font.setPixelSize(16)
        self.labelTitle.setFont(font)

        # ????????????
        self.labelClose = QLabel(
            self, cursor=Qt.PointingHandCursor, pixmap=NotificationIcon.icon(NotificationIcon.Close))

        # ????????????
        self.labelMessage = QLabel(
            message, self, cursor=Qt.PointingHandCursor, wordWrap=True, alignment=Qt.AlignLeft | Qt.AlignTop)
        font = self.labelMessage.font()
        font.setPixelSize(15)
        self.labelMessage.setFont(font)
        self.labelMessage.adjustSize()

        # ???????????????
        layout.addWidget(self.labelTitle, 0, 1)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 2)
        layout.addWidget(self.labelClose, 0, 3)
        layout.addWidget(self.labelMessage, 1, 1, 1, 2)

        # ????????????
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setColor(QColor(0, 0, 0, 25))
        effect.setOffset(4, 4)
        self.setGraphicsEffect(effect)
        self.adjustSize()

        # 5???????????????
        self._timer = QTimer(self, timeout=self.doClose)
        self._timer.setSingleShot(True)  # ???????????????
        self._timer.start(time)

    def doClose(self):
        try:
            # ??????????????????????????????item??????????????????
            self.closed[QListWidgetItem].emit(self.item)
        except:
            pass

    def mousePressEvent(self, event):
        super(NotificationItem, self).mousePressEvent(event)
        w = self.childAt(event.pos())
        if not w:
            return
        if w == self.labelClose:  # ??????????????????
            # ????????????????????????
            self._timer.stop()
            self.closed[QListWidgetItem].emit(self.item)
        elif w == self.labelMessage and self.callback and callable(self.callback):
            # ??????????????????
            self._timer.stop()
            self.closed[QListWidgetItem].emit(self.item)
            self.callback()  # ??????

    def paintEvent(self, event):
        # ?????????????????????
        super(NotificationItem, self).paintEvent(event)
        painter = QPainter(self)
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 6, 6)
        painter.fillPath(path, Qt.white)


class NotificationWindow(QListWidget):
    _instance = None

    def __init__(self, *args, **kwargs):
        super(NotificationWindow, self).__init__(*args, **kwargs)
        self.setSpacing(2)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setMinimumWidth(340)
        self.setMaximumWidth(340)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.show()
        self.animation = None
        QApplication.instance().setQuitOnLastWindowClosed(True)
        # ???????????????,?????????,?????????
        self.setWindowFlags(self.windowFlags() | Qt.Tool |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # ??????????????????
        self.setFrameShape(self.NoFrame)
        # ????????????
        self.viewport().setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # ??????????????????
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # ??????????????????
        rect = QApplication.instance().screens()[0].size()
        self.setMinimumHeight(rect.height())
        self.setMaximumHeight(rect.height())

    def removeItem(self, item):
        # ??????item
        w = self.itemWidget(item)
        self.removeItemWidget(item)
        item = self.takeItem(self.indexFromItem(item).row())
        w.close()
        w.deleteLater()
        del item

    @classmethod
    def _createInstance(cls):
        # ????????????
        if not cls._instance:
            cls._instance = NotificationWindow()
            cls._instance.show()
            NotificationIcon.init()

    @classmethod
    def info(cls, parent, title, message, callback=None, time=5000):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance, time=time,
                             ntype=NotificationIcon.Info, callback=callback)
        w.closed[QListWidgetItem].connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() - cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)
        # ??????????????????
        rect = parent.frameGeometry()
        x, y = rect.x(), rect.y()
        rect_height, rect_width = rect.height(), rect.width()
        cls._instance.move(x + (rect_width - cls._instance.width()) / 2, y - rect_height / 6)

    @classmethod
    def success(cls, parent, title, message, callback=None, time=5000):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance, time=time,
                             ntype=NotificationIcon.Success, callback=callback)
        w.closed[QListWidgetItem].connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() - cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)
        # ??????????????????
        rect = parent.frameGeometry()
        x, y = rect.x(), rect.y()
        rect_height, rect_width = rect.height(), rect.width()
        cls._instance.move(x + (rect_width - cls._instance.width()) / 2, y - rect_height / 6)

    @classmethod
    def warning(cls, parent, title, message, callback=None, time=5000):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance, time=time,
                             ntype=NotificationIcon.Warning, callback=callback)
        w.closed[QListWidgetItem].connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() - cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)
        # ??????????????????
        rect = parent.frameGeometry()
        x, y = rect.x(), rect.y()
        rect_height, rect_width = rect.height(), rect.width()
        cls._instance.move(x + (rect_width - cls._instance.width()) / 2, y - rect_height / 6)

    @classmethod
    def error(cls, parent, title, message, callback=None, time=5000):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, time=time,
                             ntype=NotificationIcon.Error, callback=callback)
        w.closed[QListWidgetItem].connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() - cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)
        # ??????????????????
        rect = parent.frameGeometry()
        x, y = rect.x(), rect.y()
        rect_height, rect_width = rect.height(), rect.width()
        cls._instance.move(x + (rect_width - cls._instance.width()) / 2, y - rect_height / 6)

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
            # ????????????????????????????????????
            self.move(event.globalPosition().toPoint() - self.m_DragPosition.toPoint())
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    layout = QHBoxLayout(w)


    def callback():
        print('????????????')


    html = "http://www.baidu.com/link?url=y_6HV07INz3pB87dC2loyHuC-GNEOJYbQuakwEO8TUDwXVu483hIodtk_3Zg0Aycnk8rzzDB5SxTWeXJk40dKa&wd=&eqid=98e086520006bdcb00000006624e7092"

    layout.addWidget(QPushButton(
        'Info', w, clicked=lambda: NotificationWindow.info(w, '??????', '????????????????????????????????????', callback=callback, time=1000)))
    layout.addWidget(QPushButton(
        'Success', w, clicked=lambda: NotificationWindow.success(w, '??????', '????????????????????????????????????', callback=callback)))
    layout.addWidget(QPushButton(
        'Warning', w, clicked=lambda: NotificationWindow.warning(
            w,
            '??????',
            '???????????????????????????????????????????????????????????????????????????',
            callback=callback)))
    layout.addWidget(QPushButton(
        'Error', w, clicked=lambda: NotificationWindow.error(
            w,
            '??????',
            f'<html><head/><body><p><span style=" font-style:italic; color:teal;">{html}</span></p></body></html>',
            callback=callback)))
    w.show()

    #     NotificationIcon.init()
    #     ww = NotificationItem('??????', '<html><head/><body><p><span style=" font-style:italic; color:teal;">????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????</span></p></body></html>', None,
    #                           ntype=NotificationIcon.Error)
    #     ww.bgWidget.setVisible(True)
    #     ww.show()
    sys.exit(app.exec())
