import sys
import time
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
    QGridLayout,
    QMessageBox
)
from PySide6.QtCore import Qt
from tasks import Task1, Task2, Task3
from string import ascii_lowercase, ascii_uppercase
import random

countPrintedTask1 = 3
countPrintedTask2 = 5
countPrintedTask3 = countPrintedTask1

class GetTime:
    @staticmethod
    def measure_time(method, *args):
        start_time = time.time()
        result = method(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

class Error_Handler:
    @staticmethod
    def show_error_message(message):
        msg = QMessageBox()
        msg.setInformativeText(message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задачи с генераторами")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Вкладка для задачи №1
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Задача №1")
        self.layout1 = QVBoxLayout()
        self.tab1.setLayout(self.layout1)

        self.label1 = QLabel("Введите целые числа a и b (a < b):")
        self.layout1.addWidget(self.label1)

        self.input_a = QTextEdit("0")
        self.input_b = QTextEdit("10")
        self.layout1.addWidget(self.input_a)
        self.layout1.addWidget(self.input_b)

        self.button1 = QPushButton("Выполнить простую реализацию")
        self.button1.clicked.connect(self.run_task1_simple)
        self.layout1.addWidget(self.button1)

        self.button1_parallel = QPushButton("Выполнить параллельную реализацию")
        self.button1_parallel.clicked.connect(self.run_task1_parallel)
        self.layout1.addWidget(self.button1_parallel)

        self.result1 = QLabel("Результат:")
        self.layout1.addWidget(self.result1)

        # Вкладка для задачи №2
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Задача №2")
        self.layout2 = QVBoxLayout()
        self.tab2.setLayout(self.layout2)

        self.button2 = QPushButton("Выполнить простую реализацию")
        self.button2.clicked.connect(self.run_task2_simple)
        self.layout2.addWidget(self.button2)

        self.button2_parallel = QPushButton("Выполнить параллельную реализацию")
        self.button2_parallel.clicked.connect(self.run_task2_parallel)
        self.layout2.addWidget(self.button2_parallel)

        self.result2 = QLabel("Результат:")
        self.layout2.addWidget(self.result2)

        # Вкладка для задачи №3
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Задача №3")
        self.layout3 = QVBoxLayout()
        self.tab3.setLayout(self.layout3)

        self.label3 = QLabel("Введите два списка целых чисел:")
        self.layout3.addWidget(self.label3)

        self.input_list1 = QTextEdit("[1, 2, 3]")
        self.input_list2 = QTextEdit("[4, 5, 6]")
        self.layout3.addWidget(self.input_list1)
        self.layout3.addWidget(self.input_list2)

        self.button3 = QPushButton("Выполнить простую реализацию")
        self.button3.clicked.connect(self.run_task3_simple)
        self.layout3.addWidget(self.button3)

        self.button3_parallel = QPushButton("Выполнить параллельную реализацию")
        self.button3_parallel.clicked.connect(self.run_task3_parallel)
        self.layout3.addWidget(self.button3_parallel)

        self.result3 = QLabel("Результат:")
        self.layout3.addWidget(self.result3)

    def run_task1_simple(self):
        try:
            a = int(self.input_a.toPlainText())
            b = int(self.input_b.toPlainText())
            if a >= b:
                Error_Handler.show_error_message("a должно быть меньше b")
                return
            task = Task1(a, b)
            result, execution_time = GetTime.measure_time(task.get_first, countPrintedTask1)
            self.result1.setText(f"Результат: {result}\nВремя выполнения: {execution_time:.4f} секунд")
        except Exception as e:
            Error_Handler.show_error_message(str(e))

    def run_task1_parallel(self):
        try:
            a = int(self.input_a.toPlainText())
            b = int(self.input_b.toPlainText())
            if a >= b:
                Error_Handler.show_error_message("a должно быть меньше b")
                return
            task = Task1(a, b)
            result, execution_time = GetTime.measure_time(task.parallel_execution, countPrintedTask1)
            self.result1.setText(f"Результат: {result}\nВремя выполнения: {execution_time:.4f} секунд")
        except Exception as e:
            Error_Handler.show_error_message(str(e))

    def run_task2_simple(self):
        try:
            chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
            task = Task2(chars)
            result, execution_time = GetTime.measure_time(task.get_first, countPrintedTask2)
            self.result2.setText(f"Результат: {result}\nВремя выполнения: {execution_time:.4f} секунд")
        except Exception as e:
            Error_Handler.show_error_message(str(e))

    def run_task2_parallel(self):
        try:
            chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
            task = Task2(chars)
            result, execution_time = GetTime.measure_time(task.parallel_execution, countPrintedTask2)
            self.result2.setText(f"Результат: {result}\nВремя выполнения: {execution_time:.4f} секунд")
        except Exception as e:
            Error_Handler.show_error_message(str(e))

    def run_task3_simple(self):
        try:
            list1 = eval(self.input_list1.toPlainText())
            list2 = eval(self.input_list2.toPlainText())
            task = Task3(list1, list2)
            result, execution_time = GetTime.measure_time(task.get_first_products, countPrintedTask3)
            self.result3.setText(f"Результат: {result}\nВремя выполнения: {execution_time:.4f} секунд")
        except Exception as e:
            Error_Handler.show_error_message(str(e))

    def run_task3_parallel(self):
        try:
            list1 = eval(self.input_list1.toPlainText())
            list2 = eval(self.input_list2.toPlainText())
            task = Task3(list1, list2)
            result, execution_time = GetTime.measure_time(task.parallel_execution, countPrintedTask3)
            self.result3.setText(f"Результат: {result}\nВремя выполнения: {execution_time:.4f} секунд")
        except Exception as e:
            Error_Handler.show_error_message(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

