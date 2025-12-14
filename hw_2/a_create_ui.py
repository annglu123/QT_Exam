from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # вызываем метод для инициализации интерфейса
        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        labelLogin = QtWidgets.QLabel("Логин")  # создаем виджет QLabel с текстом "Логин"
        labelRegistration = QtWidgets.QLabel("Пароль")  # создаем виджет QLabel с текстом "Пароль"

        self.lineEditLogin = QtWidgets.QLineEdit()  # создаем виджет QLineEdit
        self.lineEditLogin.setPlaceholderText("Введите логин")  # добавляем placeholderText "Введите логин" с помощью метода .setPlaceholderText()
        self.lineEditPassword = QtWidgets.QLineEdit()  # создаем виджет QLineEdit
        self.lineEditPassword.setPlaceholderText("Введите пароль")  # добавляем placeholderText "Введите пароль"
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # устанавливаем ограничение видимости вводимых знаков с помощью метода .setEchoMode()

        self.pushButtonLogin = QtWidgets.QPushButton()  # создаем виджет QPushButton
        self.pushButtonLogin.setText("Войти")  # устанавливаем текст "Войти" с помощью метода setText()

        self.pushButtonRegistration = QtWidgets.QPushButton()  # создаем виджет QPushButton
        self.pushButtonRegistration.setText("Регистрация")  # устанавливаем текст "Регистрация" с помощью метода setText()

        layoutLogin = QtWidgets.QHBoxLayout()  # создаем QHBoxLayout
        layoutLogin.addWidget(labelLogin)  # с помощью метода .addWidget() добавляем labelLogin
        layoutLogin.addWidget(self.lineEditLogin)  # с помощью метода .addWidget() добавляем self.lineEditLogin

        layoutPassword = QtWidgets.QHBoxLayout()  # создаем QHBoxLayout
        layoutPassword.addWidget(labelRegistration)  # с помощью метода .addWidget() добавляем labelRegistration
        layoutPassword.addWidget(self.lineEditPassword)  # с помощью метода .addWidget() добавляем self.lineEditPassword

        layoutButtons = QtWidgets.QHBoxLayout()  # создаем QHBoxLayout
        layoutButtons.addWidget(self.pushButtonLogin)  # с помощью метода .addWidget() добавляем self.pushButtonLogin
        layoutButtons.addWidget(self.pushButtonRegistration)  # с помощью метода .addWidget() добавляем self.pushButtonRegistration

        layoutMain = QtWidgets.QVBoxLayout()  # создаем QVBoxLayout
        layoutMain.addLayout(layoutLogin)  # с помощью метода .addLayout() добавляем layoutLogin
        layoutMain.addLayout(layoutPassword)  # с помощью метода .addLayout() добавляем layoutPassword
        layoutMain.addLayout(layoutButtons)  # с помощью метода .addLayout() добавляем layoutButtons

        self.setLayout(layoutMain)  # с помощью метода setLayout установливаем layoutMain на основной виджет


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
