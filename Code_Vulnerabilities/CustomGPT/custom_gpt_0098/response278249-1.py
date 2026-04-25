
import sys
from PySide.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and input fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [
            QLineEdit(), 
            QLineEdit(), 
            QTextEdit(), 
            QTextEdit(), 
            QTextEdit()
        ]

        # Add to the grid layout in 4 columns
        for index, (label, input_field) in enumerate(zip(labels, inputs)):
            row = index // 4  # Calculate row number
            column = index % 4  # Calculate column number
            gridLayout.addWidget(QLabel(label), row, column * 2)  # Labels in even columns
            gridLayout.addWidget(input_field, row, column * 2 + 1)  # Inputs in odd columns

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
