
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 250)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and fields
        elements = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add the elements to the grid layout
        for index, (label, widget) in enumerate(elements):
            row = index // 4  # determine the row number
            col = index % 4   # determine the column number
            gridLayout.addWidget(QLabel(label), row, col * 2)  # label in column
            gridLayout.addWidget(widget, row, col * 2 + 1)      # widget in next column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except Exception as e:
        print("Error:", e)
