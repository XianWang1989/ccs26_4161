
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

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

        # Add fields to the grid
        row = 0
        for index, (label, widget) in enumerate(fields):
            col = index % 4  # Distribute columns
            row = index // 4  # Move to next row if needed
            gridLayout.addWidget(QLabel(label), row, col)
            gridLayout.addWidget(widget, row, col + 1)  # Place widget next to the label

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
