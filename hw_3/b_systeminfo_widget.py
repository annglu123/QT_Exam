"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets, QtCore, QtGui
from ui.systemWidget import Ui_Form
from a_threads import SystemInfo


class SystemWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lcdNumberCPU.setStyleSheet("color: red")
        self.ui.lcdNumberRAM.setStyleSheet("color: blue")

        self.system_info_thread = SystemInfo()
        self.system_info_thread.systemInfoReceived.connect(self.update_info)
        self.ui.spinBox.valueChanged.connect(self.update_delay)
        self.system_info_thread.start()

    def update_info(self, data):
        cpu_value, ram_value = data
        self.ui.lcdNumberCPU.display(cpu_value)
        self.ui.lcdNumberRAM.display(ram_value)

    def update_delay(self):
        delay = self.ui.spinBox.value()
        # print(delay)
        self.system_info_thread.delay = delay


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemWidget()
    window.show()

    app.exec()
