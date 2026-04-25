
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)  # Adjusted size for better visibility

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        for i in range(len(labels)):
            gridLayout.addWidget(QLabel(labels[i]), i // 4, (i % 4) * 2)  # Place label
            gridLayout.addWidget(inputs[i], i // 4, (i % 4) * 2 + 1)  # Place input

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec()
    except Exception as e:
        print("Error:", e)
