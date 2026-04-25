
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Place widgets in the grid layout
        for index, (label_text, widget) in enumerate(fields):
            label = QLabel(label_text)
            gridLayout.addWidget(label, index // 4, (index % 4) * 2)  # Row, Column
            gridLayout.addWidget(widget, index // 4, (index % 4) * 2 + 1)  # Row, Column + 1

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
