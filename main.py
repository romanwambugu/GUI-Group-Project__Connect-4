from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class ConnectFour(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect Four")

        # Create the grid layout
        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)

        # Create the buttons
        self.buttons = []
        for row in range(6):
            self.buttons.append([])
            for col in range(7):
                button = QPushButton()
                button.setFixedSize(75, 75)
                self.layoutGrid.addWidget(button, row, col)
                self.buttons[row].append(button)

        # Connect the buttons to the click handler
        for row in range(6):
            for col in range(7):
                self.buttons[row][col].clicked.connect(lambda row=row, col=col: self.buttonClicked(row, col))

        # Initialize the game state
        self.current_player = 1
        self.game_over = False

    def buttonClicked(self, row, col):
        if not self.game_over:
            # Find the lowest empty row in the column
            for i in range(5, -1, -1):
                if self.buttons[i][col].text() == "":
                    # Set the button text and color
                    self.buttons[i][col].setText(str(self.current_player))
                    self.buttons[i][col].setStyleSheet(f"background-color: {'red' if self.current_player == 1 else 'yellow'}")

                    # Check for a win
                    if self.checkWin(i, col):
                        print(f"Player {self.current_player} wins!")
                        self.game_over = True
                        return

                    # Switch to the other player
                    self.current_player = 3 - self.current_player
                    return

    def checkWin(self, row, col):
        # Check for a horizontal win
        count = 0
        for i in range(7):
            if self.buttons[row][i].text() == str(self.current_player):
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check for a vertical win
        count = 0
        for i in range(6):
            if self.buttons[i][col].text() == str(self.current_player):
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check for a diagonal win (top-left to bottom-right)
        count = 0
        for i in range(-3, 4):
            if row + i < 0 or row + i >= 6 or col + i < 0 or col + i >= 7:
                continue
            if self.buttons[row+i][col+i].text() == str(self.current_player):
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check for a diagonal win (bottom-left to top-right)
        count = 0
        for i in range(-3, 4):
            if row - i < 0 or row - i >= 6 or col + i < 0 or col + i >= 7:
                continue
            if self.buttons[row-i][col+i].text() == str(self.current_player):
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        return False

if __name__ == "__main__":
    app = QApplication([])
    game = ConnectFour()
    game.show()
    app.exec_()