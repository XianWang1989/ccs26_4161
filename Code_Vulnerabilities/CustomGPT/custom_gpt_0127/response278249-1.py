
import sys
from PySide.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)  # Increased width for better layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add labels and fields to the grid layout
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

        # You can add more rows or columns if needed
        gridLayout.addWidget(QLabel("Extra Field 1"), 0, 2)
        gridLayout.addWidget(QLineEdit(), 0, 3)
        gridLayout.addWidget(QLabel("Extra Field 2"), 1, 2)
        gridLayout.addWidget(QLineEdit(), 1, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
