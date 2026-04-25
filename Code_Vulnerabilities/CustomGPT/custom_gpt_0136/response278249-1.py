
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add labels and fields
        gridLayout.addWidget(QLabel("Author"), 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        gridLayout.addWidget(QLabel("Title"), 0, 2)
        gridLayout.addWidget(QLineEdit(), 0, 3)

        gridLayout.addWidget(QLabel("Bodytext 1"), 1, 0)
        gridLayout.addWidget(QTextEdit(), 1, 1)

        gridLayout.addWidget(QLabel("Bodytext 2"), 1, 2)
        gridLayout.addWidget(QTextEdit(), 1, 3)

        gridLayout.addWidget(QLabel("Bodytext 3"), 2, 0)
        gridLayout.addWidget(QTextEdit(), 2, 1)

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
