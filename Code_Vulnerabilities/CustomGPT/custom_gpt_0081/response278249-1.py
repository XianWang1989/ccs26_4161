
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

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

        # Add spacers for columns 3 and 4 (you can use QSpacerItem if needed)
        gridLayout.addWidget(QLabel(""), 0, 2)  # Empty label for column 3
        gridLayout.addWidget(QLabel(""), 1, 2)  # Empty label for column 3
        gridLayout.addWidget(QLabel(""), 2, 2)  # Empty label for column 3
        gridLayout.addWidget(QLabel(""), 3, 2)  # Empty label for column 3
        gridLayout.addWidget(QLabel(""), 4, 2)  # Empty label for column 3

        # Column 4 (Example: add a widget if needed)
        # gridLayout.addWidget(QPushButton("Button"), 0, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("An error occurred:", str(e))
