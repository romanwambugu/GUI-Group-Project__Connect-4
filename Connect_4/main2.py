import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


'''
        buttons_per_row = 6
        buttons_per_column = 7

        for j in range(buttons_per_column):
            layout = vertical_layout_list[j]
            for i in range(buttons_per_row):
                button_number = i * buttons_per_column + j + 1
                button = QPushButton(f"Button {button_number}")
                layout.addWidget(button)
'''