
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 350, 250)

    def setLayout(self):
        gridLayout = QGridLayout(self)

        # Add form fields to the grid layout
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Set maximum columns
        max_columns = 4

        for index, (label, widget) in enumerate(fields):
            row = index // max_columns
            column = index % max_columns
            gridLayout.addWidget(QLabel(label), row, column * 2)  # Label
            gridLayout.addWidget(widget, row, column * 2 + 1)      # Widget

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.setLayout()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except Exception as e:
        print("Error:", e)
