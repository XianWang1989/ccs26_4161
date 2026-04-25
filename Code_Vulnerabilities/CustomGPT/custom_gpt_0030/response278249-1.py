
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)
        self.setLayout(self.setGridLayout())

    def setGridLayout(self):
        gridLayout = QGridLayout()

        # Define labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add fields to the grid layout
        for index, (label, field) in enumerate(fields):
            row = index // 4
            column = index % 4
            gridLayout.addWidget(QLabel(label), row, column*2)
            gridLayout.addWidget(field, row, column*2 + 1)

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except Exception as e:
        print("Error:", str(e))
