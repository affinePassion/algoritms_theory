import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QMenuBar, QMenu, QGridLayout, QWidgetAction, QComboBox
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models import Database, Plant, PlantException
from datetime import datetime
import matplotlib.dates as mdates

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Database('povt-cluster.tstu.tver.ru', 'plantSystem', 'mpi', '135a1')

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Система учета домашних растений')

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        exit_action = QWidgetAction(self)
        exit_action.triggered.connect(self.close)

    def view_table(self):
            table_type = self.table_type_combo.currentText()
            if table_type == 'Растения':
                self.update_table()
                self.table_widget.show()
                self.care_table_widget.hide()
                self.log_label.setText("Таблица Растения открыта.")
            elif table_type == 'Уход':
                self.update_care_table()
                self.table_widget.hide()
                self.care_table_widget.show()
                self.log_label.setText("Таблица Уход открыта.")
            

    
    def update_table(self):
        plants = self.db.get_plants()
        self.table_widget.setRowCount(len(plants))
        for row, plant in enumerate(plants):
            self.table_widget.setItem(row, 0, QTableWidgetItem(plant[1]))
            self.table_widget.setItem(row, 1, QTableWidgetItem(plant[2]))
            self.table_widget.setItem(row, 2, QTableWidgetItem(plant[3]))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(plant[4])))

    def update_care_table(self):
        care_records = self.db.get_care()
        self.care_table_widget.setRowCount(len(care_records))
        for row, record in enumerate(care_records):
            self.care_table_widget.setItem(row, 0, QTableWidgetItem(str(record[1])))
            self.care_table_widget.setItem(row, 1, QTableWidgetItem(record[3]))
            self.care_table_widget.setItem(row, 2, QTableWidgetItem(record[2]))
            self.care_table_widget.setItem(row, 3, QTableWidgetItem(record[4]))
 

    def create_widgets(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        # Таблица с растениями
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['Название', 'Вид', 'Последняя дата полива', 'Количество поливов'])
        layout.addWidget(self.table_widget, 2, 0, 1, 3)

        #Таблица с уходом
        self.care_table_widget = QTableWidget()
        self.care_table_widget.setRowCount(0)
        self.care_table_widget.setColumnCount(4)
        self.care_table_widget.setHorizontalHeaderLabels(['ID растения', 'Дата ухода', 'Тип ухода', 'Описание ухода'])
        layout.addWidget(self.care_table_widget, 3, 0, 1, 3)

        self.view_button = QPushButton('Открыть таблицу')
        self.view_button.clicked.connect(self.view_table)
        layout.addWidget(self.view_button, 0, 0, 1, 3)

        self.table_type_combo = QComboBox()
        self.table_type_combo.addItem('Растения')
        self.table_type_combo.addItem('Уход')
        layout.addWidget(self.table_type_combo, 1, 0, 1, 3)

        self.update_care_table()


        # Форма для добавления нового растения
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.species_input = QLineEdit()
        self.watering_date_input = QLineEdit()
        self.amount_waterings_input = QLineEdit()
        form_layout.addRow(QLabel('Название'), self.name_input)
        form_layout.addRow(QLabel('Вид'), self.species_input)
        form_layout.addRow(QLabel('Последняя дата полива'), self.watering_date_input)
        form_layout.addRow(QLabel('Количество поливов'), self.amount_waterings_input)
        layout.addLayout(form_layout, 5, 0, 1, 3)

        # Кнопка для добавления растения
        add_button = QPushButton('Добавить растение')
        add_button.clicked.connect(self.add_plant)
        layout.addWidget(add_button, 6, 0, 1, 3)

        # График активности
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas, 7, 0, 1, 3)

        # Логирование активности
        self.log_label = QLabel()
        self.log_label.adjustSize() 
        layout.addWidget(self.log_label, 9, 0, 1, 3)

        self.update_table()
        self.plot_activity()

    def add_plant(self):
        name = self.name_input.text()
        species = self.species_input.text()
        watering_date = self.watering_date_input.text()
        amount_waterings = self.amount_waterings_input.text()

        if not name or not species or not watering_date:
            self.log_label.setText("Пожалуйста, заполните все поля.")
            return

        plant = Plant(name, species, watering_date, amount_waterings)
        try:
            self.db.add_plant(plant)
            self.update_table()
            self.log_label.setText(f"Растение '{name}' добавлено успешно.")
            self.log_label.adjustSize() 
            self.name_input.clear()
            self.species_input.clear()
            self.watering_date_input.clear()
            self.amount_waterings_input.clear()
        except PlantException as e:
            self.log_label.setText(str(e))
            self.log_label.adjustSize() 

    def update_table(self):
        plants = self.db.get_plants()
        self.table_widget.setRowCount(len(plants))
        for row, plant in enumerate(plants):
            self.table_widget.setItem(row, 0, QTableWidgetItem(plant[1]))
            self.table_widget.setItem(row, 1, QTableWidgetItem(plant[2]))
            self.table_widget.setItem(row, 2, QTableWidgetItem(plant[3]))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(plant[4])))

    def plot_activity(self):
        # Получаем записи о поливах из базы данных
        watering_records = self.db.get_waterings()

        # Преобразуем даты в формат, понятный matplotlib
        dates = [datetime.strptime(record[0], '%Y-%m-%d') for record in watering_records]
        amounts = [record[1] for record in watering_records]

        # Очистка текущей фигуры
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Построение графика
        ax.plot_date(dates, amounts, linestyle='solid')

        # Настройка меток осей и заголовка
        ax.set_title('Активность поливов')
        ax.set_xlabel('Дата')
        ax.set_ylabel('Количество поливов')

        # Форматирование оси X для отображения дат
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        fig = ax.get_figure()
        fig.autofmt_xdate()  # Автоматическое форматирование дат для лучшей читаемости

        # Обновление канвы для отображения нового графика
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())