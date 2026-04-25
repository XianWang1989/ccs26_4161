
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and input fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Arrange fields in a grid layout (4 columns)
        for i, (label, widget) in enumerate(fields):
            row = i // 4  # Calculate row number
            col = i % 4   # Calculate column number
            gridLayout.addWidget(QLabel(label), row, col * 2)  # Label in even columns
            gridLayout.addWidget(widget, row, col * 2 + 1)     # Widget in odd columns

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
