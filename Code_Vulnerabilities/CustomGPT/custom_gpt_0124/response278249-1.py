
import sys
from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 200)  # Adjusted width for better layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Labels and their corresponding text fields
        items = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        for index, (label, widget) in enumerate(items):
            row = index // 4  # Determine row
            column = index % 4  # Determine column
            gridLayout.addWidget(QLabel(label), row, column * 2)  # Place label in column 0, 2
            gridLayout.addWidget(widget, row, column * 2 + 1)  # Place widget in column 1, 3

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except Exception as e:
        print("Error:", e)
