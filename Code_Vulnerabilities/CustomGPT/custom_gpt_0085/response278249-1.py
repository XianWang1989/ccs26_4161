
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Adding labels and fields to the grid layout
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Populate the grid layout
        for index, (label, widget) in enumerate(fields):
            row = index // 4  # Determine the row
            col = index % 4   # Determine the column
            gridLayout.addWidget(QLabel(label), row, col)
            gridLayout.addWidget(widget, row, col + 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
