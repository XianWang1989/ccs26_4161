
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 250)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and text fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add labels and fields to the grid layout
        for row, (label_text, widget) in enumerate(fields):
            label = QLabel(label_text)
            gridLayout.addWidget(label, row, 0)  # Column 0 for labels
            gridLayout.addWidget(widget, row, 1)  # Column 1 for inputs
            gridLayout.addWidget(QLabel(""), row, 2)  # Empty column for spacing
            gridLayout.addWidget(QLabel(""), row, 3)  # Another empty column for spacing

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec()
    except Exception as e:
        print("Error:", e)
