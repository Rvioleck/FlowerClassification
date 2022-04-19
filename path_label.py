# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QLabel


class PathLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super(PathLabel, self).__init__(*args, **kwargs)

    def update(self) -> None:
        # 仅显示100字符，超过部分截断
        self.text_len = len(self.text())
        if self.text_len > 100:
            self.setText(self.text()[0: 100] + " ...")
