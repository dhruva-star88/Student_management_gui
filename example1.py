from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


# Inherit Class
class AgeCalculator(QWidget):

    def __init__(self):
        # Call the __init__ method of parent class
        super().__init__()
        self.setWindowTitle("Age Calculator")
        # Create Grid Instance
        grid = QGridLayout()

        # Create Widgets
        name_label = QLabel("Name:")
        self.name_label_edit = QLineEdit()

        dob = QLabel("Date Of Birth MM/DD/YYYY:")
        self.dob_line_edit = QLineEdit()

        calc_button = QPushButton("Calculate Age")
        calc_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_label_edit, 0, 1)
        grid.addWidget(dob, 1, 0)
        grid.addWidget(self.dob_line_edit, 1, 1)
        grid.addWidget(calc_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # Initialize grid
        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        """--text()-- method is used to extract the valur from the Lineedit Widget"""
        date_of_birth = self.dob_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        """--setText()-- is a method of QLable """
        self.output_label.setText(f"{self.name_label_edit.text()} is {age} year old")


# To execute gui
app = QApplication(sys.argv)
age_calc = AgeCalculator()
age_calc.show()
sys.exit(app.exec())
