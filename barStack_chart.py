import sys

from PySide6.QtCharts import QChartView, QChart, QBarCategoryAxis, QBarSet, QBarSeries
from PySide6.QtCore import Qt, QRectF, QPointF, QPoint
from PySide6.QtGui import QPainter, QPen, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGraphicsProxyWidget, \
    QGraphicsLineItem


class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, bars):
        self.titleLabel.setText(title)
        for bar, value in bars:
            if bar not in self.Cache:
                item = ToolTipItem(
                    bar.color(),
                    (bar.label() or "-") + ":" + str(value), self)
                self.layout().addWidget(item)
                self.Cache[bar] = item
            else:
                self.Cache[bar].setText(
                    (bar.label() or "-") + ":" + str(value))
            brush = bar.brush()
            color = brush.color()
            self.Cache[bar].setVisible(color.alphaF() == 1.0)  # 隐藏那些不可用的项
        self.adjustSize()  # 调整大小


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        self.setWidget(self.tipWidget)
        self.hide()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def show(self, title, bars, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, bars)
        super(GraphicsProxyWidget, self).show()


class BarWidget(QChartView):

    def __init__(self, *args, **kwargs):
        self.flowers = ["叶子花", "康乃馨", "雏  菊", "蒲公英", "栀子花", "木槿花", "绣球花",
                        "鸢尾花", "丁香花", "百合花", "荷  花", "牵牛花", "桃  花", "牡丹花",
                        "蝴蝶兰", "梅  花", "玫瑰花", "樱  花", "向日葵", "郁金香"]
        self.flower_words = ["bougainvillea", "carnation", "daisy", "dandelion", "gardenia", "hibiscus", "hydrangea",
                             "iris", "lilac", "lily", "lotus", "morningglory", "peachflower", "peony", "phalaenopsis",
                             "plumblossom", "rose", "sakura", "sunflower", "tulip"]
        super(BarWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.setWindowTitle("各文件夹花朵图像预测结果——柱状堆叠图")
        icon = QIcon()
        icon.addFile(u"images/堆叠柱状图.png")
        self.setWindowIcon(icon)
        self.data = {}
        self.initChart()

    def addData(self, directory, res):
        if directory in self.data.keys():
            if res in self.data[directory].keys():
                self.data[directory][res] += 1
            else:
                self.data[directory][res] = 1
        else:
            self.data[directory] = {}
            self.data[directory][res] = 1

    def clearData(self):
        self.data = {}

    def mouseMoveEvent(self, event):
        super(BarWidget, self).mouseMoveEvent(event)
        pos = event.position()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round(x)
        # 得到在坐标系中的所有bar的类型和点
        serie = self._chart.series()[0]
        bars = [(bar, bar.at(index))
                for bar in serie.barSets() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        #         print(bars)
        if bars:
            right_top = self._chart.mapToPosition(
                QPointF(self.max_x, self.max_y))
            # 等分距离比例
            step_x = round(
                (right_top.x() - self.point_top.x()) / self.category_len)
            posx = self._chart.mapToPosition(QPointF(x, self.min_y))
            self.lineItem.setLine(posx.x(), self.point_top.y(),
                                  posx.x(), posx.y())
            self.lineItem.show()
            try:
                title = self.categories[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, bars, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        # bar透明度
        brush = bar.brush()
        color = brush.color()
        alpha = 0.0 if color.alphaF() == 1.0 else 1.0
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar.setBrush(brush)
        # marker
        brush = marker.labelBrush()
        color = brush.color()
        alpha = 0.4 if color.alphaF() == 1.0 else 1.0
        # 设置label的透明度
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker的透明度
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

    def handleMarkerHovered(self, status):
        # 设置bar的画笔宽度
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def handleBarHoverd(self, status, index):
        # 设置bar的画笔宽度
        bar = self.sender()  # 信号发送者
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="柱状图堆叠详细结果")
        self._chart.setAcceptHoverEvents(True)
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = list(self.data.keys())
        names = self.flowers
        series = QBarSeries(self._chart)
        for i, name in enumerate(names):
            bar = QBarSet(name)
            # 随机数据
            for category in self.categories:
                try:
                    bar.append(self.data[category][self.flower_words[i]])
                except KeyError as e:
                    print(e)
                    bar.append(0)
            series.append(bar)
            bar.hovered.connect(self.handleBarHoverd)  # 鼠标悬停
        self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        # x轴
        axis_x = QBarCategoryAxis(self._chart)
        axis_x.append(self.categories)
        self._chart.setAxisX(axis_x, series)
        # chart的图例
        legend = self._chart.legend()
        legend.setVisible(True)
        # 遍历图例上的标记并绑定信号
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.handleMarkerClicked)
            # 鼠标悬停事件
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)
        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # line 宽度需要调整
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.category_len = len(axisX.categories())
        self.min_x, self.max_x = -0.5, self.category_len - 0.5
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = BarWidget()
    view.show()
    sys.exit(app.exec())
