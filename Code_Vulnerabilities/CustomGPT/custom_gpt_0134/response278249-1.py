
import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)  # Adjusted size for better layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Row 1
        gridLayout.addWidget(QLabel("Author"), 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        # Row 2
        gridLayout.addWidget(QLabel("Title"), 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1)

        # Row 3
        gridLayout.addWidget(QLabel("Bodytext 1"), 2, 0)
        gridLayout.addWidget(QTextEdit(), 2, 1)

        # Row 4
        gridLayout.addWidget(QLabel("Bodytext 2"), 3, 0)
        gridLayout.addWidget(QTextEdit(), 3, 1)

        # Row 5
        gridLayout.addWidget(QLabel("Bodytext 3"), 4, 0)
        gridLayout.addWidget(QTextEdit(), 4, 1)

        # Adding Spaces for Columns
        gridLayout.addWidget(QLabel(""))  # Empty label for spacing
        gridLayout.addWidget(QLabel(""))  # Empty label for spacing

        # Add more labels/fields to expand into the desired columns
        gridLayout.addWidget(QLabel("Col 1"), 0, 2)  # Placeholder for additional columns
        gridLayout.addWidget(QLineEdit(), 0, 3)

        # Finalize layout
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
