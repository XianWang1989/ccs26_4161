
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and fields
        labels = [
            "Author", "Title", "Bodytext 1", 
            "Bodytext 2", "Bodytext 3"
        ]
        fields = [
            QLineEdit(), QLineEdit(), 
            QTextEdit(), QTextEdit(), QTextEdit()
        ]

        # Add labels and fields to the grid layout
        for i in range(len(labels)):
            row = i // 4  # Calculate row number
            column = i % 4  # Calculate column number
            gridLayout.addWidget(QLabel(labels[i]), row, column * 2)  # Set label
            gridLayout.addWidget(fields[i], row, column * 2 + 1)  # Set field

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("An error occurred:", e)
