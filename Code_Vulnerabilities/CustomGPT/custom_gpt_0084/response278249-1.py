
import sys
from PySide.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add labels and line edits to the grid layout
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
    except Exception as e:
        print("Error:", e)
