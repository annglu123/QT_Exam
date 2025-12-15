import os

from PySide6 import QtWidgets, QtCore, QtGui

ROOT_FOLDER = os.getcwd()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        #
        label = QtWidgets.QLabel()
        label.setObjectName("image_label")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        icon_path = os.path.join(ROOT_FOLDER, 'static', 'ico', "64.png")
        if os.path.exists(icon_path):
            label.setPixmap(QtGui.QPixmap(icon_path))
        else:
            label.setText("Изображение не найдено")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
