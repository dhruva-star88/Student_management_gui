from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, \
    QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout
from PyQt6.QtGui import QAction
import sys
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_action = QAction("Add", self)
        add_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_action)

        help_action = QAction("About", self)
        help_menu_item.addAction(help_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_table(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.id = QLineEdit()
        self.id.setPlaceholderText("Enter The Student ID...")
        layout.addWidget(self.id)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter Name...")
        layout.addWidget(self.name)

        self.course_name = QComboBox()
        courses = ["Biology", "Maths", "Physics", "Chemistry"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile_nr = QLineEdit()
        self.mobile_nr.setPlaceholderText("Enter Mobile Number...")
        layout.addWidget(self.mobile_nr)

        submit = QPushButton("Submit")
        submit.clicked.connect(self.add_student)
        layout.addWidget(submit)

        self.setLayout(layout)

    def add_student(self):
        id_nr = self.id.text()
        name = self.name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile_nr = self.mobile_nr.text()

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (id, name, course, mobile_nr) VALUES (?,?,?,?)", (id_nr, name, course, mobile_nr))
        connection.commit()
        cursor.close()
        connection.close()
        main_win.load_table()


app = QApplication(sys.argv)
main_win = MainWindow()
main_win.load_table()
main_win.show()
sys.exit(app.exec())
