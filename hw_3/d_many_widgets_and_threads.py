"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from b_systeminfo_widget import SystemWidget
from c_weatherapi_widget import WeatherWidget


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.systemWidget = SystemWidget()
        self.weatherWidget = WeatherWidget()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.systemWidget)
        layout.addWidget(self.weatherWidget)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()