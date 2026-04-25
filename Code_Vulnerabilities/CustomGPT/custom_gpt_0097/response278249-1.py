
import sys
from PySide2.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and input fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add fields to grid layout
        for row, (label, widget) in enumerate(fields):
            col = row % 4  # Place up to 4 items in a row
            gridLayout.addWidget(QLabel(label), row // 4, col * 2)  # Label column
            gridLayout.addWidget(widget, row // 4, col * 2 + 1)  # Widget column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("Error:", e)
