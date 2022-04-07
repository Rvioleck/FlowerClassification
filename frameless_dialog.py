# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget, \
    QGraphicsDropShadowEffect, QPushButton, QGridLayout, QSpacerItem, \
    QSizePolicy, QApplication, QCheckBox

from ui_framelessDialog import Ui_frameless_dialog

Stylesheet = """
#Custom_Widget {
    background: white;
    border-radius: 10px;
}

#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: white;
    background: red;
}
"""


class Dialog(QDialog, Ui_frameless_dialog):

    def __init__(self, parent_style, rect=None, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.initUi()
        self.setupUi(self)
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(Stylesheet)
        # 设置checkbox和pushButton样式表
        for checkbox in self.findChildren(QCheckBox):
            checkbox.setStyleSheet(parent_style)
        self.pushButton.setStyleSheet(parent_style)
        self.radioButton.setStyleSheet(parent_style)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        # 设置透明度
        self.setWindowOpacity(0.9)
        # 设置位置
        if rect is not None:
            self.move(rect.x() + (rect.width() - self.size().width()) / 2,
                      rect.y() + (rect.height() - self.size().height()) / 2)

    def initUi(self):
        layout = QVBoxLayout(self)
        # 重点： 这个widget作为背景和圆角
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout.addWidget(self.widget)

        # 在widget中添加ui
        layout = QGridLayout(self.widget)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        layout.addWidget(QPushButton(
            'r', self, clicked=self.accept, objectName='closeButton'), 0, 1)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum,
                                   QSizePolicy.Expanding), 1, 0)

    def sizeHint(self):
        return QSize(self.size())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressX = event.position().x()  # 记录鼠标按下的时候的坐标
            self.pressY = event.position().y()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.drag = True

    def mouseMoveEvent(self, event):
        if self.drag:
            x = event.position().x()
            y = event.position().y()  # 获取移动后的坐标
            move_x = x - self.pressX
            move_y = y - self.pressY  # 计算移动了多少
            position_x = self.frameGeometry().x() + move_x
            position_y = self.frameGeometry().y() + move_y  # 计算移动后主窗口在桌面的位置
            self.move(position_x, position_y)  # 移动主窗口

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.drag = False


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Dialog()
    w.exec()
    QTimer.singleShot(200, app.quit)
    sys.exit(app.exec())
