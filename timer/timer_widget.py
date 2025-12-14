import sys
import time
from PySide6.QtCore import (QTimer, Qt, QTime)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLineEdit, QTimeEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QLabel, QMessageBox, QAbstractItemView)


# --- 1. Класс для представления данных таймера ---
class TimerData:
    def __init__(self, name, duration_seconds):
        self.id = str(time.time())
        self.name = name
        self.full_duration = duration_seconds
        self.seconds_left = duration_seconds
        self.status = "Остановлен"
        self.is_running = False
        self.qtimer = None
        # --- НОВЫЕ ПОЛЯ: Прямые ссылки на виджеты ячеек ---
        self.item_seconds_left = None
        self.item_status = None
        self.item_name = None
        self.item_duration = None


# --- 2. Основной класс приложения (ГИП) ---

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение для нескольких таймеров (QTimer в UI-потоке, PySide6)")
        self.setGeometry(100, 100, 900, 400)
        # Словарь {timer_id: TimerData object} для хранения всех данных таймеров
        self.timers = {}
        # Словарь {timer_id: row_index} все еще нужен для удаления строк
        self.timer_rows = {}

        self.init_ui()

    def init_ui(self):
        # ... (Код UI остается прежним) ...
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # --- Панель ввода нового таймера ---
        input_layout = QHBoxLayout()
        self.name_input = QLineEdit(placeholderText="Название таймера")
        self.duration_input = QTimeEdit()
        self.duration_input.setDisplayFormat("mm:ss")
        self.duration_input.setTime(QTime(0, 5, 0))
        self.add_button = QPushButton("Добавить таймер")
        self.add_button.clicked.connect(self.add_timer_ui)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(QLabel("Длительность:"))
        input_layout.addWidget(self.duration_input)
        input_layout.addWidget(self.add_button)
        main_layout.addLayout(input_layout)

        # --- Кнопки управления всеми таймерами ---
        control_layout = QHBoxLayout()
        self.start_all_button = QPushButton("Старт всех")
        self.start_all_button.clicked.connect(self.start_all_timers)
        self.pause_all_button = QPushButton("Пауза всех")
        self.pause_all_button.clicked.connect(self.pause_all_timers)
        self.reset_all_button = QPushButton("Сброс всех")
        self.reset_all_button.clicked.connect(self.reset_all_timers)
        control_layout.addWidget(self.start_all_button)
        control_layout.addWidget(self.pause_all_button)
        control_layout.addWidget(self.reset_all_button)
        main_layout.addLayout(control_layout)

        # --- Таблица таймеров ---
        self.table = QTableWidget(0, 7)
        headers = ['Название', 'Полная длит.', 'Осталось', 'Статус', '', '', '']
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        main_layout.addWidget(self.table)

        # --- Статус бар ---
        self.status_label = QLabel("Активных таймеров: 0")
        main_layout.addWidget(self.status_label)

    # --- Вспомогательные функции UI для форматирования времени ---
    def format_seconds(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02}:{secs:02}"

    def update_status_bar(self):
        active_count = sum(1 for timer in self.timers.values() if timer.is_running)
        self.status_label.setText(f"Активных таймеров: {active_count}")

    # --- Методы логики таймеров (в UI-потоке) ---

    def add_timer_ui(self):
        name = self.name_input.text() or f"Таймер {len(self.timers) + 1}"
        time_val = self.duration_input.time()
        duration_seconds = time_val.minute() * 60 + time_val.second()

        new_timer_data = TimerData(name, duration_seconds)
        self.timers[new_timer_data.id] = new_timer_data

        # Создаем QTimer специально для этого таймера
        qtimer = QTimer(self)
        qtimer.setInterval(1000)
        qtimer.timeout.connect(lambda tid=new_timer_data.id: self.update_timer(tid))
        new_timer_data.qtimer = qtimer

        # --- СОЗДАНИЕ UI И СОХРАНЕНИЕ ССЫЛОК НА ЯЧЕЙКИ ---
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.timer_rows[new_timer_data.id] = row_position

        # Создаем QTableWidgetItem и сохраняем на него ссылку в TimerData
        new_timer_data.item_name = QTableWidgetItem(name)
        new_timer_data.item_duration = QTableWidgetItem(self.format_seconds(duration_seconds))
        new_timer_data.item_seconds_left = QTableWidgetItem(self.format_seconds(duration_seconds))
        new_timer_data.item_status = QTableWidgetItem(new_timer_data.status)

        self.table.setItem(row_position, 0, new_timer_data.item_name)
        self.table.setItem(row_position, 1, new_timer_data.item_duration)
        self.table.setItem(row_position, 2, new_timer_data.item_seconds_left)
        self.table.setItem(row_position, 3, new_timer_data.item_status)
        # --- КОНЕЦ СОХРАНЕНИЯ ССЫЛОК ---

        start_btn = QPushButton("Старт")
        start_btn.clicked.connect(lambda checked, tid=new_timer_data.id: self.start_timer(tid))
        pause_btn = QPushButton("Пауза")
        pause_btn.clicked.connect(lambda checked, tid=new_timer_data.id: self.pause_timer(tid))
        reset_btn = QPushButton("Сброс")
        reset_btn.clicked.connect(lambda checked, tid=new_timer_data.id: self.reset_timer(tid))
        delete_btn = QPushButton("Удалить")
        delete_btn.clicked.connect(lambda checked, tid=new_timer_data.id: self.remove_timer(tid))

        self.table.setCellWidget(row_position, 4, start_btn)
        self.table.setCellWidget(row_position, 5, pause_btn)
        self.table.setCellWidget(row_position, 6, delete_btn)
        self.update_status_bar()

    def update_timer(self, timer_id):
        """Слот, вызываемый QTimer каждую секунду."""
        timer = self.timers.get(timer_id)
        if timer and timer.is_running and timer.seconds_left > 0:
            timer.seconds_left -= 1
            # --- ИСПОЛЬЗУЕМ ПРЯМУЮ ССЫЛКУ ---
            timer.item_seconds_left.setText(self.format_seconds(timer.seconds_left))

            if timer.seconds_left == 0:
                self.handle_timer_finished(timer_id)

    def set_timer_status_ui(self, timer_id, status, is_running):
        timer = self.timers.get(timer_id)
        if timer:
            timer.is_running = is_running
            timer.status = status
            # --- ИСПОЛЬЗУЕМ ПРЯМУЮ ССЫЛКУ ---
            timer.item_status.setText(status)

            if status == "Идёт":
                color = Qt.GlobalColor.green
            elif status == "Завершён":
                color = Qt.GlobalColor.red
            else:
                color = Qt.GlobalColor.white

            # --- ИСПОЛЬЗУЕМ ПРЯМЫЕ ССЫЛКИ ДЛЯ ПОДСВЕТКИ ---
            timer.item_name.setBackground(color)
            timer.item_duration.setBackground(color)
            timer.item_seconds_left.setBackground(color)
            timer.item_status.setBackground(color)

            self.update_status_bar()

    def handle_timer_finished(self, timer_id):
        self.pause_timer(timer_id)
        self.set_timer_status_ui(timer_id, "Завершён", is_running=False)
        name = self.timers[timer_id].name
        QMessageBox.information(self, "Таймер завершен!", f"Таймер '{name}' завершил работу.")

    def start_timer(self, timer_id):
        timer = self.timers.get(timer_id)
        if timer and not timer.is_running and timer.seconds_left > 0:
            self.set_timer_status_ui(timer_id, "Идёт", is_running=True)
            timer.qtimer.start()  # Запуск QTimer

    def pause_timer(self, timer_id):
        timer = self.timers.get(timer_id)
        if timer:
            self.set_timer_status_ui(timer_id, "На паузе", is_running=False)
            timer.qtimer.stop()

    def reset_timer(self, timer_id):
        timer = self.timers.get(timer_id)
        if timer:
            self.pause_timer(timer_id)
            timer.seconds_left = timer.full_duration
            self.set_timer_status_ui(timer_id, "Сброшен", is_running=False)
            # --- ИСПОЛЬЗУЕМ ПРЯМУЮ ССЫЛКУ ---
            timer.item_seconds_left.setText(self.format_seconds(timer.seconds_left))

    def remove_timer(self, timer_id):
        if timer_id in self.timers:
            self.pause_timer(timer_id)
            timer = self.timers[timer_id]
            if timer.qtimer:
                timer.qtimer.deleteLater()

            row = self.timer_rows[timer_id]
            self.table.removeRow(row)
            # --- УДАЛЯЕМ ВСЕ ССЫЛКИ ИЗ СЛОВАРЕЙ ---
            del self.timers[timer_id]
            del self.timer_rows[timer_id]
            self.update_status_bar()

    # --- Управление всеми таймерами ---
    def start_all_timers(self):
        for timer_id in list(self.timers.keys()):
            self.start_timer(timer_id)

    def pause_all_timers(self):
        for timer_id in list(self.timers.keys()):
            self.pause_timer(timer_id)

    def reset_all_timers(self):
        for timer_id in list(self.timers.keys()):
            self.reset_timer(timer_id)

    # reindex_rows метод удален, так как больше не нужен

    def closeEvent(self, event):
        self.pause_all_timers()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec())