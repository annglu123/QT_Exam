from PySide6 import QtCore, QtGui, QtWidgets

# Список доступных цветов в палитре
COLORS = [
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QtWidgets.QPushButton):
    """
    Кастомный виджет кнопки, представляющий собой кружок определенного цвета.
    """

    def __init__(self, color):
        super().__init__()

        self.color = color
        self.setFixedSize(QtCore.QSize(24, 24))
        self.setStyleSheet(f"border: 1px solid black; border-radius: 12px; background-color: {self.color};")

        self.setCheckable(True)

    def setActivate(self):
        """Визуально выделяет кнопку, когда она активна (выбрана)."""
        self.setStyleSheet(f"border: 3px solid white; border-radius: 10px; background-color: {self.color};")

    def setDeactivate(self):
        """Возвращает кнопку в нормальное состояние."""
        self.setStyleSheet(f"border: 1px solid black; border-radius: 10px; background-color: {self.color};")


class Canvas(QtWidgets.QLabel):
    """
    Виджет холста для рисования. Использует QPixmap для хранения изображения.
    """

    def __init__(self):
        super().__init__()

        self.pen_color = QtGui.QColor('#000000')
        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill(QtGui.QColor("white"))
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None

    def set_pen_color(self, color):
        """Устанавливает новый цвет пера для рисования."""
        self.pen_color = QtGui.QColor(color)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """Обрабатывает движение мыши для рисования линии."""
        if self.last_x is None:  # Если это первое движение (начало линии)
            self.last_x = event.position().x()
            self.last_y = event.position().y()
            return  # Игнорируем его, чтобы не было линии от предыдущего места клика

        # Начинаем рисование на QPixmap
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(4)  # Толщина линии
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, event.position().x(), event.position().y())
        painter.end()  # Завершаем рисование
        self.setPixmap(canvas)  # Обновляем отображение QLabel

        # Обновляем координаты предыдущей точки
        self.last_x = event.position().x()
        self.last_y = event.position().y()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """Сбрасывает координаты при отпускании кнопки мыши."""
        self.last_x = None
        self.last_y = None


class Window(QtWidgets.QWidget):
    """
    Основное окно приложения, управляющее холстом и палитрой.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self) -> None:
        """Инициализация Ui"""
        self.canvas = Canvas()
        self.palette_layout = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(self.palette_layout)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addLayout(self.palette_layout)

        self.setLayout(layout)

    def add_palette_buttons(self, layout):
        """Создает кнопки палитры и добавляет их в макет."""
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c: self.canvas.set_pen_color(c))
            b.clicked.connect(self.chooseButton)
            layout.addWidget(b)

    def chooseButton(self):
        """Обрабатывает выбор кнопки, визуально выделяя ее и деактивируя остальные."""
        layout = self.palette_layout

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()

            if widget is self.sender():
                widget.setActivate()
                continue
            widget.setDeactivate()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
