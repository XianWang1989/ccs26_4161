
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 175)
        self.setLayout(self.createLayout())

    def createLayout(self):
        gridLayout = QGridLayout()

        # Adding labels and text fields to the grid layout
        gridLayout.addWidget(QLabel("Author:"), 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        gridLayout.addWidget(QLabel("Title:"), 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1)

        gridLayout.addWidget(QLabel("Bodytext 1:"), 2, 0)
        gridLayout.addWidget(QTextEdit(), 2, 1)

        gridLayout.addWidget(QLabel("Bodytext 2:"), 3, 0)
        gridLayout.addWidget(QTextEdit(), 3, 1)

        gridLayout.addWidget(QLabel("Bodytext 3:"), 4, 0)
        gridLayout.addWidget(QTextEdit(), 4, 1)

        # Adjust column spans as needed to fill up to 4 columns
        # For example, you can make the text edits span multiple columns
        for i in range(2, 5):
            gridLayout.addWidget(QTextEdit(), i, 2)

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
