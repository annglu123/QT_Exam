"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import datetime
import sys

from PySide6 import QtWidgets, QtGui, QtCore

from ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.window_size()
        self.display_size()
        self.initSignals()

    def window_size(self):
        qr = self.frameGeometry()
        size = (qr.width(), qr.height())
        #print(f'windows_size: {size}')
        # print(QtGui.QGuiApplication.screens()[0].size().toTuple())
        return size

    def display_size(self):
        ds = QtGui.QGuiApplication.primaryScreen().availableGeometry().bottomRight().toTuple()
        # print(f'display_size: {ds}')
        return ds

    def initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenterClicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)

    def onPushButtonLTClicked(self):
        self.move(0, 0)

    def onPushButtonLBClicked(self):
        self.move(0, self.display_size()[1] - self.window_size()[1])

    def onPushButtonRTClicked(self):
        self.move(self.display_size()[0] - self.window_size()[0], 0)

    def onPushButtonRBClicked(self):
        self.move(self.display_size()[0] - self.window_size()[0], self.display_size()[1] - self.window_size()[1])

    def onPushButtonCenterClicked(self):
        self.move((self.display_size()[0] - self.window_size()[0])/2, (self.display_size()[1] - self.window_size()[1])/2)

    def onPushButtonMoveCoordsClicked(self):
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onPushButtonGetDataClicked(self):
        self.ui.plainTextEdit.setPlainText(f'Текущее время: {datetime.datetime.now().date()} {datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second} \n'
                                           f'Количество экранов: {len(QtGui.QGuiApplication.screens())},\n'
                                           f'Разрешение экрана: {QtGui.QGuiApplication.screens()[0].size().toTuple()},\n'
                                           f'Размеры окна: {self.frameGeometry().width()} x {self.frameGeometry().height()},\n'
                                           f'Минимальные размеры окна: {self.minimumWidth()} x {self.minimumHeight()},\n'
                                           f'{self.windowState()},\n'
                                           f'Текущие координаты окна: {self.frameGeometry().getCoords()},\n'
                                           f'Окно находится на мониторе: {QtGui.QGuiApplication.primaryScreen().name()}, \n'
                                           f'{QtGui.QGuiApplication.focusWindow()}')


        print(len(QtGui.QGuiApplication.screens()))  # количество экранов

        print(QtGui.QGuiApplication.screens()[0].size().toTuple())  # разрешение экрана
        print(self.frameGeometry())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
