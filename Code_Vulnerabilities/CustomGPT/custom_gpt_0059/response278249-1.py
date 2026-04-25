
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

    def setLayout(self):
        gridLayout = QGridLayout(self)

        # Define form elements
        labels = [
            QLabel("Author"),
            QLabel("Title"),
            QLabel("Bodytext 1"),
            QLabel("Bodytext 2"),
            QLabel("Bodytext 3"),
        ]
        inputs = [
            QLineEdit(),
            QLineEdit(),
            QTextEdit(),
            QTextEdit(),
            QTextEdit(),
        ]

        # Add elements to the grid layout
        for i in range(len(labels)):
            gridLayout.addWidget(labels[i], i // 4, (i % 4) * 2)
            gridLayout.addWidget(inputs[i], i // 4, (i % 4) * 2 + 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setLayout()
    mainWindow.show()
    sys.exit(app.exec_())
