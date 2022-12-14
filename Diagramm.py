from PySide6.QtCharts import QChart, QLineSeries, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QDateTime


class Diagramm(QChartView):
    def __init__(self, parent):
        super(Diagramm, self).__init__(parent)

        self.axis_time = QDateTimeAxis()
        self.axis_time.setTitleText("Zeitachse")
        self.axis_time.setTickCount(7)
        self.axis_time.setRange(QDateTime.currentDateTime(), QDateTime.currentDateTime().addDays(7))

        self.axis_percent = QValueAxis()
        self.axis_percent.setTitleText("Prozent")
        self.axis_percent.setRange(0, 100)

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("x-Achse")
        self.axis_x.setRange(0, 5)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("y-Achse")
        self.axis_y.setRange(0, 20)

        self.chart = QChart()

        self.setChart(self.chart)


        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_time, Qt.AlignTop)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.chart.addAxis(self.axis_percent, Qt.AlignRight)

        self.series = QSplineSeries()
        self.chart.addSeries(self.series)
        self.series.setName("f(x) = x^2")
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        self.series.append(0, 0)
        self.series.append(1, 1)
        self.series.append(2, 4)
        self.series.append(3, 9)
        self.series.append(4, 16)
        self.series.append(5, 25)

        self.series_2 = QLineSeries()
        self.chart.addSeries(self.series_2)
        self.series_2.attachAxis(self.axis_time)
        self.series_2.attachAxis(self.axis_percent)

        self.series_2.setName("Prozent über Zeit")

        self.series_2.append(QDateTime.currentDateTime().toMSecsSinceEpoch(), 0)
        self.series_2.append(QDateTime.currentDateTime().addDays(1).toMSecsSinceEpoch(), 100)
        self.series_2.append(QDateTime.currentDateTime().addDays(5).toMSecsSinceEpoch(), 10)
        self.series_2.append(QDateTime.currentDateTime().addDays(6).toMSecsSinceEpoch(), 25)

