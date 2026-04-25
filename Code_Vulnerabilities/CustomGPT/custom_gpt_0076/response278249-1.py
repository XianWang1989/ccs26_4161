
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define the labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add fields to the grid layout
        for i, (label_text, widget) in enumerate(fields):
            label = QLabel(label_text)
            gridLayout.addWidget(label, i // 4, (i % 4) * 2)  # Place label
            gridLayout.addWidget(widget, i // 4, (i % 4) * 2 + 1)  # Place field

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("Error:", e)
