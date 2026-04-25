
import sys
from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)
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

        # Place them in the grid layout
        for i, (label, widget) in enumerate(fields):
            row = i // 4  # Determine the row
            col = i % 4   # Determine the column
            gridLayout.addWidget(QLabel(label), row * 2, col)  # Labels occupy their own row
            gridLayout.addWidget(widget, row * 2 + 1, col)      # Fields below the labels

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(app.exec())
    except Exception as e:
        print("Error:", e)
