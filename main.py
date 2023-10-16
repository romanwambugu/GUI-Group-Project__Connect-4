#Importing the compenents we need
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect Four")

        # Create vertical layouts for each group of buttons
        v_layout1 = QVBoxLayout()
        v_layout2 = QVBoxLayout()
        v_layout3 = QVBoxLayout()
        v_layout4 = QVBoxLayout()
        v_layout5 = QVBoxLayout()
        v_layout6 = QVBoxLayout()
        v_layout7 = QVBoxLayout()

        vertical_layout_list = [v_layout1, v_layout2, v_layout3, v_layout4, v_layout5, v_layout6, v_layout7]

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")
        button7 = QPushButton("Button 7")

        clickable_buttons = [button1, button2, button3, button4, button5, button6, button7]


# Add every clickable button to every vertical layout using a loop
        for i, layout in enumerate(vertical_layout_list):
            button = QPushButton(f"Button {i+1}")
            layout.addWidget(button)

            


        # Create a horizontal layout and add the vertical layouts to it
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout1)
        h_layout.addLayout(v_layout2)
        h_layout.addLayout(v_layout3)
        h_layout.addLayout(v_layout4)
        h_layout.addLayout(v_layout5)
        h_layout.addLayout(v_layout6)
        

        # Set the horizontal layout as the layout for the widget
        self.setLayout(h_layout)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.resize(1920, 1080)
    widget.show()
    app.exec()