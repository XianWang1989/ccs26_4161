
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Adding labels and line edits to the layout
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

        # Example of adding more columns
        for i in range(4):
            gridLayout.addWidget(QLabel(f"Extra Field {i + 1}"), i, 2)
            gridLayout.addWidget(QLineEdit(), i, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("Error:", e)
