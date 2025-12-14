import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtWidgets
from main_window import MainWindow

app = QtWidgets.QApplication()

# window = QWidget()
# window.setWindowTitle('Простейшее окно')
# window.show()

window = MainWindow()
window.show()

app.exec()

# после выполнения этой команды никакие другие выполняться не будут
# sys.exit(app.exec())

# если нужно выполнение следующих команд после закрытия окна
# app.exec()
print('Новая запись')