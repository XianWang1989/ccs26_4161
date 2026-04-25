
import sys
from PySide.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)  # Adjusted size for more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and line edits
        labels = [
            QLabel("Author"), QLabel("Title"), QLabel("Bodytext 1"),
            QLabel("Bodytext 2"), QLabel("Bodytext 3")
        ]
        lineEdits = [
            QLineEdit(), QLineEdit(),
            QTextEdit(), QTextEdit(), QTextEdit()
        ]

        # Add to grid layout
        for i in range(len(labels)):
            row = i // 4  # Calculate the row
            column = i % 4  # Calculate the column
            gridLayout.addWidget(labels[i], row, column * 2)  # Labels in even columns
            gridLayout.addWidget(lineEdits[i], row, column * 2 + 1)  # Fields in odd columns

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
