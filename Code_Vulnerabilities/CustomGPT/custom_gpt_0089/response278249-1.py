
import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 175)

        self.SetLayout()

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

        # Add elements to the grid layout
        gridLayout.addWidget(labelAuthor, 0, 0)
        gridLayout.addWidget(txtAuthor, 0, 1)
        gridLayout.addWidget(labelTitle, 0, 2)
        gridLayout.addWidget(txtTitle, 0, 3)
        gridLayout.addWidget(labelBodytext1, 1, 0)
        gridLayout.addWidget(txtBodytext1, 1, 1, 1, 3)  # Span across multiple columns
        gridLayout.addWidget(labelBodytext2, 2, 0)
        gridLayout.addWidget(txtBodytext2, 2, 1, 1, 3)
        gridLayout.addWidget(labelBodytext3, 3, 0)
        gridLayout.addWidget(txtBodytext3, 3, 1, 1, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except Exception as e:
        print("Error:", e)
