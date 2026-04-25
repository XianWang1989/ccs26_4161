
import sys
from PySide2.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Labels and Text Fields
        elements = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Place elements in the grid
        for i, (label_text, widget) in enumerate(elements):
            label = QLabel(label_text)
            gridLayout.addWidget(label, i // 4, (i % 4) * 2)  # Label position
            gridLayout.addWidget(widget, i // 4, (i % 4) * 2 + 1)  # Widget position

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
