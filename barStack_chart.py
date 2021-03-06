# -*- coding: utf-8 -*-

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
            self.Cache[bar].setVisible(color.alphaF() == 1.0)  # ???????????????????????????
        self.adjustSize()  # ????????????


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
        self.flowers = ["?????????", "?????????", "???  ???", "?????????", "?????????", "?????????", "?????????",
                        "?????????", "?????????", "?????????", "???  ???", "?????????", "???  ???", "?????????",
                        "?????????", "???  ???", "?????????", "???  ???", "?????????", "?????????"]
        self.flower_words = ["bougainvillea", "carnation", "daisy", "dandelion", "gardenia", "hibiscus", "hydrangea",
                             "iris", "lilac", "lily", "lotus", "morningglory", "peachflower", "peony", "phalaenopsis",
                             "plumblossom", "rose", "sakura", "sunflower", "tulip"]
        super(BarWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # ?????????
        self.setWindowTitle("?????????????????????????????????????????????????????????")
        icon = QIcon()
        icon.addFile(u"images/???????????????.png")
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
        # ??????????????????????????????????????????xy???
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round(x)
        # ??????????????????????????????bar???????????????
        serie = self._chart.series()[0]
        bars = [(bar, bar.at(index))
                for bar in serie.barSets() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        #         print(bars)
        if bars:
            right_top = self._chart.mapToPosition(
                QPointF(self.max_x, self.max_y))
            # ??????????????????
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
            # ??????????????????????????????????????????tip??????
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # ??????????????????????????????????????????tip??????
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, bars, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()  # ???????????????
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        # bar?????????
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
        # ??????label????????????
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # ??????marker????????????
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

    def handleMarkerHovered(self, status):
        # ??????bar???????????????
        marker = self.sender()  # ???????????????
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
        # ??????bar???????????????
        bar = self.sender()  # ???????????????
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="???????????????????????????")
        self._chart.setAcceptHoverEvents(True)
        # Series??????
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = list(self.data.keys())
        names = self.flowers
        series = QBarSeries(self._chart)
        for i, name in enumerate(names):
            bar = QBarSet(name)
            # ????????????
            for category in self.categories:
                try:
                    bar.append(self.data[category][self.flower_words[i]])
                except KeyError as e:
                    print(e)
                    bar.append(0)
            series.append(bar)
            bar.hovered.connect(self.handleBarHoverd)  # ????????????
        self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # ??????????????????
        # x???
        axis_x = QBarCategoryAxis(self._chart)
        axis_x.append(self.categories)
        self._chart.setAxisX(axis_x, series)
        # chart?????????
        legend = self._chart.legend()
        legend.setVisible(True)
        # ???????????????????????????????????????
        for marker in legend.markers():
            # ????????????
            marker.clicked.connect(self.handleMarkerClicked)
            # ??????????????????
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)
        # ??????widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # line ??????????????????
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # ???????????????????????????mouseMoveEvent???????????????
        # ??????x???y?????????????????????
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.category_len = len(axisX.categories())
        self.min_x, self.max_x = -0.5, self.category_len - 0.5
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # ???????????????????????????
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = BarWidget()
    view.show()
    sys.exit(app.exec())
