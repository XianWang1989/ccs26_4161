
import sys
from PySide.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add form fields to the grid layout
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        row = 0
        for i, (label, widget) in enumerate(fields):
            gridLayout.addWidget(QLabel(label), row, i % 4)  # Add label
            gridLayout.addWidget(widget, row + 1, i % 4)     # Add corresponding widget

            if (i + 1) % 4 == 0:  # Move to the next row after 4 columns
                row += 2

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
