
import sys
from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 175)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and fields
        fields = {
            "Author": QLineEdit(),
            "Title": QLineEdit(),
            "Bodytext 1": QTextEdit(),
            "Bodytext 2": QTextEdit(),
            "Bodytext 3": QTextEdit()
        }

        # Adding fields to the grid layout
        row = 0
        column = 0
        for label, widget in fields.items():
            gridLayout.addWidget(QLabel(label), row, column)
            gridLayout.addWidget(widget, row + 1, column)
            column += 1
            if column >= 4:  # Move to next row after four columns
                column = 0
                row += 2  # Move down by 2 to leave space for labels

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec())
    except SystemExit:
        print("Closing Window...")
    except Exception as e:
        print(e)
