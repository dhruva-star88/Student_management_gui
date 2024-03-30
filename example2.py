from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QPushButton, QLineEdit, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.dist_label_edit = QLineEdit()

        time_label = QLabel("Time(hours):")
        self.time_label_edit = QLineEdit()

        self.options = QComboBox()
        self.options.addItems(["Metric(km)", "Imperial(miles)"])

        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.dist_label_edit, 0, 1)
        grid.addWidget(self.options, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calc_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.dist_label_edit.text())
        time = float(self.time_label_edit.text())
        speed = distance / time

        if self.options.currentText() == "Metric(km)":
            speed = round(speed, 2)
            unit = "km/hr"
        if self.options.currentText() == "Imperial(miles)":
            speed = round(speed * 0.63214, 2)
            unit = "mph"

        self.output_label.setText(f"Average Speed:  {speed} {unit}")


app = QApplication(sys.argv)
speed_calc = SpeedCalculator()
speed_calc.show()
sys.exit(app.exec())
