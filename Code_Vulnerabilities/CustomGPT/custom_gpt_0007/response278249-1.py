
import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 175)  # Adjust window size for better layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and text fields
        labelAuthor = QLabel("Author")
        txtAuthor = QLineEdit()
        labelTitle = QLabel("Title")
        txtTitle = QLineEdit()
        labelBodytext1 = QLabel("Bodytext 1")
        txtBodytext1 = QTextEdit()
        labelBodytext2 = QLabel("Bodytext 2")
        txtBodytext2 = QTextEdit()
        labelBodytext3 = QLabel("Bodytext 3")
        txtBodytext3 = QTextEdit()

        # Add widgets to the grid layout
        gridLayout.addWidget(labelAuthor, 0, 0)  # Row 0, Column 0
        gridLayout.addWidget(txtAuthor, 0, 1)    # Row 0, Column 1
        gridLayout.addWidget(labelTitle, 0, 2)   # Row 0, Column 2
        gridLayout.addWidget(txtTitle, 0, 3)     # Row 0, Column 3

        gridLayout.addWidget(labelBodytext1, 1, 0)  # Row 1, Column 0
        gridLayout.addWidget(txtBodytext1, 1, 1, 1, 3)  # Row 1, Column 1, span 1 row and 3 columns
        gridLayout.addWidget(labelBodytext2, 2, 0)  # Row 2, Column 0
        gridLayout.addWidget(txtBodytext2, 2, 1, 1, 3)  # Row 2, Column 1, span 1 row and 3 columns
        gridLayout.addWidget(labelBodytext3, 3, 0)  # Row 3, Column 0
        gridLayout.addWidget(txtBodytext3, 3, 1, 1, 3)  # Row 3, Column 1, span 1 row and 3 columns

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
