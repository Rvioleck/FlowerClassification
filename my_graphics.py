from PySide6.QtCore import QRectF, Qt, Signal, QPointF
from PySide6.QtGui import QColor, QPixmap, QPen, QTransform
from PySide6.QtWidgets import QGraphicsView, QGraphicsPixmapItem, QGraphicsScene, QGraphicsItem
from tensorflow import image as img
from PIL import ImageQt, Image

class GraphicsView(QGraphicsView):
    save_signal = Signal(bool)
    img_signal = Signal(int)
    img_rotation_signal = Signal(int)
    img_attribute_signal = Signal(float, int, float, int)

    def __init__(self, picture, parent=None):
        super(GraphicsView, self).__init__(parent)

        self.img_signal[int].connect(self.update_img)
        self.img_rotation_signal[int].connect(self.rotate_img)
        self.img_attribute_signal[float, int, float, int].connect(self.updte_img_attribute)
        # 设置放大缩小时跟随鼠标
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.picture = QPixmap(picture)
        self.image_item = GraphicsPixmapItem(self.picture)
        self.pixmap = self.image_item.pixmap()
        self.image_item.setFlag(QGraphicsItem.ItemIsMovable)
        self.scene.addItem(self.image_item)

        size = self.image_item.pixmap().size()
        # 调整图片在中间
        self.image_item.setPos(-size.width() / 2, -size.height() / 2)
        self.scale(0.2, 0.2)

    def update_img(self, tag):
        image = self.image_item.pixmap().toImage()
        if tag == 0:
            trans = QTransform()
            trans.rotate(90)
            new_image = image.transformed(trans, Qt.SmoothTransformation)
            self.image_item.setPixmap(QPixmap.fromImage(new_image))
            self.pixmap = self.image_item.pixmap()
        elif tag == 1:
            trans = QTransform()
            trans.rotate(270)
            new_image = image.transformed(trans, Qt.SmoothTransformation)
            self.image_item.setPixmap(QPixmap.fromImage(new_image))
            self.pixmap = self.image_item.pixmap()
        elif tag == 2:
            new_image = image.mirrored(True, False)
            self.image_item.setPixmap(QPixmap.fromImage(new_image))
            self.pixmap = self.image_item.pixmap()
        elif tag == 3:
            new_image = image.mirrored(False, True)
            self.image_item.setPixmap(QPixmap.fromImage(new_image))
            self.pixmap = self.image_item.pixmap()

    def rotate_img(self, dial_value):
        print(dial_value)
        self.image_item.setScale(dial_value / 50)

    def updte_img_attribute(self, brightness, contrast, hue, saturation):
        image = ImageQt.fromqpixmap(self.pixmap)
        if brightness != 0:
            image = Image.fromarray(img.adjust_brightness(image, brightness).numpy())  # 调整亮度
        if contrast != 0:
            image = Image.fromarray(img.adjust_contrast(image, contrast).numpy())  # 调整对比度
        if hue != 0:
            image = Image.fromarray(img.adjust_hue(image, hue).numpy())  # 调整色相
        if saturation != 0:
            image = Image.fromarray(img.adjust_saturation(image, saturation).numpy())  # 调整饱和度
        self.image_item.setPixmap(ImageQt.toqpixmap(image))

    def update_img_brightness(self, rate):
        if rate == 0:
            self.image_item.setPixmap(self.pixmap)
        image = ImageQt.fromqpixmap(self.pixmap)
        new_image = Image.fromarray(img.adjust_brightness(image, rate).numpy())
        self.image_item.setPixmap(ImageQt.toqpixmap(new_image))

    def update_img_contrast(self, rate):
        if rate == 0:
            self.image_item.setPixmap(self.pixmap)
        image = ImageQt.fromqpixmap(self.pixmap)
        new_image = Image.fromarray(img.adjust_contrast(image, rate).numpy())
        self.image_item.setPixmap(ImageQt.toqpixmap(new_image))

    def wheelEvent(self, event):
        '''滚轮事件'''
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

    def mouseReleaseEvent(self, event):
        '''鼠标释放事件'''
        # print(self.image_item.is_finish_cut, self.image_item.is_start_cut)
        if self.image_item.is_finish_cut:
            self.save_signal[bool].emit(True)
        else:
            self.save_signal[bool].emit(False)


class GraphicsPixmapItem(QGraphicsPixmapItem):
    save_signal = Signal(bool)

    def __init__(self, pixmap, parent=None):
        super(GraphicsPixmapItem, self).__init__(parent)

        self.setPixmap(pixmap)
        self.is_start_cut = False
        self.current_point = None
        self.is_finish_cut = False
        x, y = self.boundingRect().x(), self.boundingRect().y()
        w, h = self.boundingRect().width(), self.boundingRect().height()
        self.item_start = QPointF(x, y)
        self.item_end = QPointF(x + w, y + h)
        self.start_point = self.item_start
        self.end_point = self.item_end

    def mouseMoveEvent(self, event):
        '''鼠标移动事件'''
        self.current_point = event.pos()
        if not self.is_start_cut or self.is_midbutton:
            self.moveBy(self.current_point.x() - self.start_point.x(),
                        self.current_point.y() - self.start_point.y())
            self.is_finish_cut = False
        self.update()

    def mousePressEvent(self, event):
        '''鼠标按压事件'''
        super(GraphicsPixmapItem, self).mousePressEvent(event)
        self.start_point = event.pos()
        self.current_point = None
        self.is_finish_cut = False
        if event.button() == Qt.MiddleButton:
            self.is_midbutton = True
            self.update()
        else:
            self.is_midbutton = False
            self.update()

    def paint(self, painter, QStyleOptionGraphicsItem, QWidget):
        super(GraphicsPixmapItem, self).paint(painter, QStyleOptionGraphicsItem, QWidget)
        try:
            if self.is_start_cut and not self.is_midbutton:
                # print(self.start_point, self.current_point)
                if not self.current_point:
                    return
                # 绘制截图框
                pen = QPen(Qt.DashLine)
                pen.setColor(QColor(88, 155, 255, 240))
                pen.setWidth(1)
                painter.setPen(pen)
                painter.setBrush(QColor(255, 255, 255, 100))
                painter.drawRect(QRectF(self.start_point, self.current_point))
                self.end_point = self.current_point
                self.is_finish_cut = True
        except AttributeError as e:
            print(e)
