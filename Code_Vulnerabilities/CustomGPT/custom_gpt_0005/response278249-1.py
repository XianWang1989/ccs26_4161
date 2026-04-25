
import sys
from PySide.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and text fields
        labels = [
            QLabel("Author"), QLabel("Title"), 
            QLabel("Bodytext 1"), QLabel("Bodytext 2"), 
            QLabel("Bodytext 3")
        ]
        textFields = [
            QLineEdit(), QLineEdit(), 
            QTextEdit(), QTextEdit(), 
            QTextEdit()
        ]

        # Add labels and text fields to the grid layout
        for i in range(len(labels)):
            row = i // 4  # Determine the row index
            column = i % 4  # Determine the column index
            gridLayout.addWidget(labels[i], row, column * 2)  # Labels in even columns
            gridLayout.addWidget(textFields[i], row, column * 2 + 1)  # Text fields in odd columns

        # Set the layout for the main window
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
