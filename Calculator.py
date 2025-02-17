import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.result_display = QLineEdit(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon("Calculator-icon.png"))

        v_layout = QVBoxLayout()
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setFont(QFont('Calibri', 24))
        v_layout.addWidget(self.result_display)

        #Buttons for the calculator
        grid_layout = QGridLayout()
        buttons = [
            ('C', '(', ')', '%'),
            ('sqrt', '1/x', '**', 'pi'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            
        ]

        #Adding buttons to the grid
        row, col = 0, 0
        for button_row in buttons:
            for button_text in button_row:
                button = QPushButton(button_text)
                button.setFont(QFont('Arial', 18))
                # button.setFixedSize(80, 80)
                button.clicked.connect(self.on_button_click)
                grid_layout.addWidget(button, row, col)
                col += 1
            row += 1
            col = 0

        # Add the grid layout to the main vertical layout
        v_layout.addLayout(grid_layout)

        # Set the layout for the window
        self.setLayout(v_layout)

        # Apply styles via QSS (Qt Style Sheets)
        self.setStyleSheet("""
                            QWidget {
                                background-color: #2e2e2e;
                            }
                            QLineEdit {
                                background-color: #444444;
                                border: 2px solid #666666;
                                padding: 10px;
                                font-size: 50px;
                                font-weight: bold;
                                color: white;
                            }
                            QPushButton {
                                background-color: #555555;
                                color: white;
                                border-radius: 10px;
                                padding: 20px;
                                margin: 5px;
                                font-size: 18px;
                            }
                            QPushButton:hover {
                                background-color: #666666;
                            }
                            QPushButton:pressed {
                                background-color: #777777;
                            }
                        """)

    #this function is for handling button clicks from the app
    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        #Handle "=" button (evaluate the expression)
        if button_text == "=":
            try:
                expression = self.result_display.text()
                expression = expression.replace("pi", str(3.14159265359))
                result = str(eval(expression))  #Evaluate the expression safely
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText("Error")
        
        #Handle "C" button(clear the display)
        elif button_text == "C":
            self.result_display.clear()
        
        #Handle other button presses (numbers, operators, etc.)
        else:
            current_text = self.result_display.text()
            new_text = current_text + button_text
            self.result_display.setText(new_text)

    #This function is for handling key presses i.e., keyboard inputs
    def keyPressEvent(self, event):
        key = event.key() #the key code for example, Qt.Key_A, Qt.Key_Enter, Qt.Key_9
        key_text = event.text() #The text of the key (e.g., "A", "1") is retrieved

        #Handle keyboard input for numbers and operators
        if key_text.isdigit() or key_text in "+-*/.()":
            self.result_display.setText(self.result_display.text() + key_text)

        #Handle "Enter" or "Return" key to evaluate the expression
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            self.evaluate_expression()

        # Handle "Backspace" key to delete the last character
        elif key == Qt.Key_Backspace:
            current_text = self.result_display.text()
            self.result_display.setText(current_text[:-1])

        # Handle "Esc" key to clear the display
        elif key == Qt.Key_Escape or key == Qt.Key_C:
            self.result_display.clear()

    def evaluate_expression(self):
        """Evaluate the expression on the display"""
        try:
            expression = self.result_display.text()
            expression = expression.replace("pi", str(3.14159265359))
            result = str(eval(expression))  # Evaluate the expression safely
            self.result_display.setText(result)
        except Exception as e:
            self.result_display.setText("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())