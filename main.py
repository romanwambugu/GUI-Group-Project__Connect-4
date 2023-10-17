#Importing the compenents we need
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout , QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect Four")

        grid_formation = [   "Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7",
                             "", "", "", "", "", "", "",
                             "", "", "", "", "", "", "",
                             "", "", "", "", "", "", "",
                             "", "", "", "", "", "", "",
                             "", "", "", "", "", "", "",
                             "", "", "", "", "", "", ""   ]
        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)

        positions = [(r, c) for r in range(7) for c in range(7)]
        for position, coordinate in zip(positions, grid_formation):
            button = QPushButton(coordinate)
            button.setFixedSize(250, 150)  # Set the size of the button
            layoutGrid.addWidget(button, *position)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.resize(800, 600)  # Adjust the size of the window
    window.show()
    app.exec()