from PySide6 import QtWidgets, QtGui
from static import res

res.qInitResources()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        pushButton = QtWidgets.QPushButton()
        pushButton.setObjectName("my_action_button")
        icon = QtGui.QIcon(":/ico/ico/icons8-джейк-16.png")
        pushButton.setIcon(icon)
        layout.addWidget(pushButton)

        label = QtWidgets.QLabel()
        label.setObjectName("status_label_gif")
        pixmap = QtGui.QPixmap(":/gif/gif/load_2.gif")
        label.setPixmap(pixmap)
        layout.addWidget(label)

        self.setLayout(layout)

        self.perform_check_without_self()

    def perform_check_without_self(self):
        found_button = self.findChild(QtWidgets.QPushButton, "my_action_button")

        found_label = self.findChild(QtWidgets.QLabel, "status_label_gif")

        if found_button and found_label:
            print(f"Кнопка найдена! Текст на ней: {found_button.text()}")
            # Можно взаимодействовать с найденным объектом
            found_button.setEnabled(False)
            print("Метка найдена!")
        else:
            print("Не удалось найти элементы по именам объектов.")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
