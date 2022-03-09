import sys

from PySide6.QtCharts import QChartView, QChart, QPieSeries, QPieSlice
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QBrush
from PySide6.QtWidgets import QApplication, QToolTip


class PieWidget(QChartView):
    flowers = ["杜鹃花", "叶子花", "康乃馨", "雏  菊", "蒲公英", "栀子花", "木槿花",
               "绣球花", "鸢尾花", "丁香花", "百合花", "荷  花", "牵牛花", "水仙花",
               "桃  花", "牡丹花", "蝴蝶兰", "玫瑰花", "樱  花", "向日葵", "郁金香"]

    flower_words = ["azalea", "bougainvillea", "carnation", "daisy", "dandelion", "gardenia", "hibiscus",
                    "hydrangea", "iris", "lilac", "lily", "lotus", "morningglory", "narcissus",
                    "peachflower", "peony", "phalaenopsis", "rose", "sakura", "sunflower", "tulip"]

    colors = [(222, 60, 60), (255, 148, 217), (218, 187, 171), (241, 203, 6), (96, 67, 1), (187, 187, 187),
              (227, 58, 91),
              (169, 177, 232), (153, 69, 253), (216, 158, 221), (176, 197, 122), (106, 135, 89), (28, 77, 183),
              (249, 245, 138),
              (224, 189, 213), (189, 115, 121), (185, 73, 79), (120, 0, 20), (181, 97, 127), (205, 134, 18),
              (240, 96, 140)]

    def __init__(self, parent=None, *args, **kwargs):
        super(PieWidget, self).__init__(parent, *args, **kwargs)
        # 抗锯齿
        self.setBackgroundBrush(QBrush(QColor(210, 224, 232)))
        self.setRenderHint(QPainter.Antialiasing)
        self.portion = kwargs.pop('portion', None)
        self.setVisible(False)
        self.initChart()

    def setPortion(self, portion):
        self.portion = portion

    def addPortion(self, portion):
        for i in range(0, len(self.flowers)):
            self.portion[i] += portion[i]

    def initChart(self, model_name=""):
        chart = QChart()
        # font = QFont()
        # font.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        # font.setPointSize(14)
        # font.setBold(True)
        # chart.setFont(font)
        chart.setBackgroundBrush(QBrush(QColor(235, 241, 224)))
        chart.addSeries(self.getSeries())
        chart.createDefaultAxes()
        # 设置动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setAnimationDuration(500)
        # 设置标题
        chart.setTitle("{}模型预测结果".format(model_name))
        chart.legend().setVisible(False)
        # 对齐方式
        chart.legend().setAlignment(Qt.AlignRight)
        self.setToolTip(self.getToolTip())
        self.setChart(chart)

    def hoveredEvent(self, slice, state):
        if not state:
            self.setToolTip(self.getToolTip())
            return
        for per in self.series.slices():
            if per.isExploded() and per is not self.series.slices()[self.index]:
                per.setExploded(False)  # 突出显示，设置颜色
                per.setLabelVisible(False)  #
                per.setPen(QPen(Qt.white, 1))
        slice.setExplodeDistanceFactor(0.1)
        slice.setExploded(True)  # 突出显示，设置颜色
        slice.setLabelVisible(True)  #
        slice.setPen(QPen(Qt.darkBlue, 1))
        whole = sum(self.portion)
        i = self.series.slices().index(slice)
        toolTip = "<p style='white-space:pre'>"  # 富文本标签
        img_path = u"images/flowers/{}.png".format(self.flower_words[i])
        toolTip += '<img src={} height="24" width="24"><b><font color={}>{}:{:.4%}</font></b>\n'.format(
            img_path, self.__rgb2html(self.colors[i]), self.flowers[i], self.portion[i] / whole)
        toolTip += "</p>"  # 富文本结束标签
        self.setToolTip(toolTip)

    def getToolTip(self):
        index = self.portion.index(max(self.portion))
        whole = sum(self.portion)
        if whole == 0:
            return "未开始预测"
        QToolTip.setFont(QFont("oldEnglish", 10))
        toolTip = "<p style='white-space:pre'>"  # 富文本标签
        for i in range(0, len(self.portion)):
            img_path = u"images/flowers/{}.png".format(self.flower_words[i])
            if i == index:
                toolTip += '<img src={} height="24" width="24"><b><font color={}>{}:{:.4%}</font></b>\n'.format(
                    img_path, self.__rgb2html(self.colors[i]), self.flowers[i], self.portion[i] / whole)
            else:
                toolTip += '<img src={} height="24" width="24"><font color={}>{}:{:.4%}</font>\n'.format(
                    img_path, self.__rgb2html(self.colors[i]), self.flowers[i], self.portion[i] / whole)
        toolTip += "</p>"  # 富文本结束标签
        return toolTip

    @staticmethod
    def __rgb2html(color):
        # RGB颜色转HTML颜色
        number = '#'
        for i in color:
            shu = hex(int(i))[2:]
            if len(shu) < 2:
                shu = '0' + shu
            number += shu
        return number

    def getSeries(self):
        index = self.portion.index(max(self.portion))
        self.index = index
        self.series = QPieSeries()
        for i in range(0, len(self.portion)):
            slice = self.series.append(self.flowers[i], self.portion[i])  # 遍历每个扇区
            slice.setColor(QColor(self.colors[i][0], self.colors[i][1], self.colors[i][2]))  # 设置扇区颜色
            slice.setBorderColor(QColor(self.colors[i][0], self.colors[i][1], self.colors[i][2]))  # 设置扇区边缘颜色
            slice.setLabelColor(QColor(self.colors[i][0], self.colors[i][1], self.colors[i][2]))  # 设置扇区标签颜色
            font = QFont()
            font.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
            font.setPointSize(13)
            font.setBold(True)
            slice.setLabelFont(font)
            slice.setLabelArmLengthFactor(0.1)  # 设置扇区臂长占比
            if i == index:  # 特殊处理最大扇区
                slice.setExploded(True)  # 突出显示，设置颜色
                slice.setLabelVisible(True)  #
                slice.setPen(QPen(Qt.darkBlue, 2))
        # 设置扇形图组件内占比
        self.series.setPieSize(0.7)
        self.series.hovered[QPieSlice, bool].connect(self.hoveredEvent)
        return self.series


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pieWidget = PieWidget(portion=[2, 3, 5])
    pieWidget.setRenderHint(QPainter.Antialiasing)
    pieWidget.show()
    sys.exit(app.exec())