
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)  # Adjust width for more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and text fields
        field_data = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add fields to the grid layout
        for index, (label, widget) in enumerate(field_data):
            row = index // 4
            column = index % 4
            gridLayout.addWidget(QLabel(label), row, column * 2)    # Label at even column
            gridLayout.addWidget(widget, row, column * 2 + 1)       # Widget at next column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
