"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
from PySide6 import QtWidgets
from ui.weather import Ui_Form
from a_threads import WeatherHandler


class WeatherWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.weather_info = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.setCheckable(True)

        self.ui.pushButton.clicked.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self, status):
        if status:
            self.ui.pushButton.setText("Остановить")
            self.weather_info = WeatherHandler(self.ui.doubleSpinBoxLatitude.value(), self.ui.doubleSpinBoxLongitude.value())
            self.weather_info.setDelay(self.ui.spinBox.value())
            self.weather_info.weatherReceived.connect(self.text_information)

            self.ui.doubleSpinBoxLatitude.setDisabled(True)
            self.ui.doubleSpinBoxLongitude.setDisabled(True)
            self.ui.spinBox.setDisabled(True)
            self.weather_info.start()

        else:
            self.weather_info.status = status
            self.ui.pushButton.setText("Получить погоду")
            self.ui.doubleSpinBoxLatitude.setDisabled(False)
            self.ui.doubleSpinBoxLongitude.setDisabled(False)
            self.ui.spinBox.setDisabled(False)


    def text_information(self, data):
        print(data)
        current_temperature = str(data["current_weather"]["temperature"])
        current_windspeed = str(data["current_weather"]["windspeed"])
        current_weather = f'Текущая температура: {current_temperature}, скорость ветра: {current_windspeed} км/ч'
        self.ui.plainTextEdit.appendPlainText(current_weather)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WeatherWidget()
    window.show()

    app.exec()
