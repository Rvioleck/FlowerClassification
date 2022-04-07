# -*- coding: utf-8 -*-

import os.path
import re
from io import BytesIO

from PIL import Image
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from bs4 import BeautifulSoup, element
from requests import get


class ImageLabel(QLabel):
    pixmap_signal = Signal(bool, str, QPixmap)

    def __init__(self, *args, **kwargs):
        super(ImageLabel, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setScaledContents(True)
        self.my_pixmap = None
        self.effect_shadow = QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(5, 5)  # 偏移
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
        if event.mimeData().hasImage():  # 如果有图片数据，直接使用图片
            url = event.mimeData().text()
            self.my_pixmap = QPixmap(event.mimeData().imageData())
            tag = True
        elif event.mimeData().hasUrls():  # 如果有url数据，解析url
            text = event.mimeData().text()
            url = text.split("file:///")[-1]
            if not os.path.exists(url):
                url = text.split("file:/")[-1]
            if not os.path.exists(url):
                url = text.split("file:/")[-1].replace("%20", " ")
            self.my_pixmap = QPixmap(url)
            tag = False
            if self.my_pixmap.isNull():
                # 从网页URL提取图片
                self.my_pixmap = get_image_from_url(url)  # 从url中解析img标签中含src属性的jpg格式的图片资源
                tag = True
        print("pixmap=" + str(self.my_pixmap))
        print("url=" + url)
        self.pixmap_signal[bool, str, QPixmap].emit(tag, url, self.my_pixmap)
        event.acceptProposedAction()


def get_image_from_url(url: str):
    headers = {  # 伪装头
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    request = get(url=url,
                  headers=headers
                  )
    soup = BeautifulSoup(request.content, "html.parser")  # 解析html
    img_tags = soup.find_all(re.compile("img"))  # 匹配img标签
    pixmap = QPixmap()
    for tag in img_tags:  # type: element.Tag
        if tag.has_attr("src"):  # 存在src属性
            img_src = tag.attrs["src"]  # 获取src属性的内容
            path, name = os.path.split(img_src)
            if name.split(".")[-1] == "jpg":  # 资源后缀为jpg的资源
                img_url = "https:" + img_src  # 拼接完整的url
                print("img_url=" + img_url)
                pixmap.loadFromData(get(img_url, headers=headers).content)  # 加载pixmap
                return pixmap
    # 若无img标签、src属性或jpg资源，尝试直接解析图片
    try:
        pixmap = Image.open(BytesIO(get(url, headers=headers).content)).toqpixmap()
    except Exception as e:
        print(e.args)
    finally:
        return pixmap
