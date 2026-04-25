
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

    def setLayout(self):
        gridLayout = QGridLayout(self)

        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        for index, (label, widget) in enumerate(fields):
            row = index // 4  # Calculate the row number
            column = index % 4  # Calculate the column number
            gridLayout.addWidget(QLabel(label), row, column * 2)  # Add label at even column
            gridLayout.addWidget(widget, row, column * 2 + 1)  # Add widget at odd column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setLayout()
    mainWindow.show()
    sys.exit(app.exec_())
