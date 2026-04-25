
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 300)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add labels and fields in a grid layout
        gridLayout.addWidget(QLabel("Author"), 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        gridLayout.addWidget(QLabel("Title"), 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1)

        gridLayout.addWidget(QLabel("Bodytext 1"), 2, 0)
        gridLayout.addWidget(QTextEdit(), 2, 1)

        gridLayout.addWidget(QLabel("Bodytext 2"), 3, 0)
        gridLayout.addWidget(QTextEdit(), 3, 1)

        gridLayout.addWidget(QLabel("Bodytext 3"), 4, 0)
        gridLayout.addWidget(QTextEdit(), 4, 1)

        # Optionally, add more columns
        # You can split the layout into multiple parts to simulate columns
        gridLayout.addWidget(QLabel("Some Other Field"), 0, 2)
        gridLayout.addWidget(QLineEdit(), 0, 3)

        # You can add more rows and fields as necessary
        # Add an additional field directly to the right of the existing layout
        gridLayout.addWidget(QLabel("Extra Info"), 1, 2)
        gridLayout.addWidget(QTextEdit(), 1, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except Exception as e:
        print("An error occurred:", e)
