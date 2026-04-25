
import sys
from PySide2.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and input fields
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

        # Add widgets to grid layout
        gridLayout.addWidget(labelAuthor, 0, 0)  # Row 0, Column 0
        gridLayout.addWidget(txtAuthor, 0, 1)     # Row 0, Column 1
        gridLayout.addWidget(labelTitle, 0, 2)    # Row 0, Column 2
        gridLayout.addWidget(txtTitle, 0, 3)      # Row 0, Column 3

        gridLayout.addWidget(labelBodytext1, 1, 0)  # Row 1, Column 0
        gridLayout.addWidget(txtBodytext1, 1, 1)     # Row 1, Column 1
        gridLayout.addWidget(labelBodytext2, 1, 2)    # Row 1, Column 2
        gridLayout.addWidget(txtBodytext2, 1, 3)      # Row 1, Column 3

        gridLayout.addWidget(labelBodytext3, 2, 0)  # Row 2, Column 0
        gridLayout.addWidget(txtBodytext3, 2, 1)     # Row 2, Column 1

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
