"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore

from ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.ui.lcdNumber.setDigitCount(7)
        self.ui.dial.setMinimum(0)
        self.ui.dial.setMaximum(100)
        self.ui.comboBox.addItems(["dec", "oct", "hex", "bin"])

    def initSignals(self):
        self.ui.comboBox.currentIndexChanged.connect(self.calculation)
        self.ui.dial.valueChanged.connect(self.LCDandConsole)
        self.ui.horizontalSlider.valueChanged.connect(self.setValueDial)
        self.ui.dial.valueChanged.connect(self.setValueHorizontalSlider)

    def LCDandConsole(self):
        self.ui.lcdNumber.display(self.ui.dial.value())
        print(self.ui.comboBox.currentText())
        if self.ui.comboBox.currentText() == 'oct':
            print(oct(int(self.ui.lcdNumber.value())))
        elif self.ui.comboBox.currentText() == 'hex':
            print(hex(int(self.ui.lcdNumber.value())))
        elif self.ui.comboBox.currentText() == 'bin':
            print(bin(int(self.ui.lcdNumber.value())))
        elif self.ui.comboBox.currentText() == 'dec':
            print(int(self.ui.lcdNumber.value()))

    def calculation(self):
        print(self.ui.comboBox.currentText())
        if self.ui.comboBox.currentText() == "oct":
            self.ui.lcdNumber.setOctMode()
        elif self.ui.comboBox.currentText() == "hex":
            self.ui.lcdNumber.setHexMode()
        elif self.ui.comboBox.currentText() == "bin":
            self.ui.lcdNumber.setBinMode()
        elif self.ui.comboBox.currentText() == "dec":
            self.ui.lcdNumber.setDecMode()

    def setValueDial(self):
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        # print(self.ui.horizontalSlider.value())
        # print(bin(self.ui.horizontalSlider.value()))

    def setValueHorizontalSlider(self):
        self.ui.horizontalSlider.setValue(self.ui.dial.value())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Plus:
            self.ui.dial.triggerAction(self.ui.dial.SliderAction.SliderSingleStepAdd)
        elif event.key() == QtCore.Qt.Key.Key_Minus:
            self.ui.dial.triggerAction(self.ui.dial.SliderAction.SliderSingleStepSub)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
