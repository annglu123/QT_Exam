from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Новое приложение')
        self.resize(300, 200)