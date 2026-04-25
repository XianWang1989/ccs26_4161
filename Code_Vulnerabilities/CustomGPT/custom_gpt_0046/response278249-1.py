
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 250)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and corresponding input fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add fields to the grid layout
        for i, (label, widget) in enumerate(fields):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)
            gridLayout.addWidget(widget, i // 4, (i % 4) * 2 + 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("Error:", e)
