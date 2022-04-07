# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QMouseEvent
from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):

    def __init__(self, *args, **kwargs):
        QMenuBar.__init__(self, *args, **kwargs)
        self.drag = False

    def mousePressEvent(self, event: QMouseEvent):
        print(self.actionAt(event.position().toPoint()))
        # 鼠标点击的区域为action或menu区域，则正常执行
        if self.actionAt(event.position().toPoint()) in \
                [self.parent().menu.menuAction(),
                 self.parent().menu_M.menuAction(),
                 self.parent().menu_help.menuAction(),
                 self.parent().pinAction, self.parent().lowerAction, self.parent().closeAction]:
            super().mousePressEvent(event)
        # 鼠标点击区域为其他区域，则进行拖拽
        elif event.button() == Qt.LeftButton:
            self.pressX = event.position().x()  # 记录鼠标按下的时候的坐标
            self.pressY = event.position().y()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.drag = True

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.drag:
            x = event.position().x()
            y = event.position().y()  # 获取移动后的坐标
            move_x = x - self.pressX
            move_y = y - self.pressY  # 计算移动了多少
            position_x = self.parent().frameGeometry().x() + move_x
            position_y = self.parent().frameGeometry().y() + move_y  # 计算移动后主窗口在桌面的位置
            # self.move(position_x, position_y)  # 移动主窗口
            self.parent().move(position_x, position_y)  # 移动主窗口

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.drag = False
