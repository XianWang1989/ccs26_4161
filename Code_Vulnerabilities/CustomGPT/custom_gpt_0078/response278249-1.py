
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add fields to the grid layout
        for index, (label, widget) in enumerate(fields):
            row = index // 4  # which row
            column = index % 4  # which column
            gridLayout.addWidget(QLabel(label), row, column * 2)  # label at position
            gridLayout.addWidget(widget, row, column * 2 + 1)  # widget at position

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print("Error:", e)
