
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        edits = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        for i, (label, edit) in enumerate(zip(labels, edits)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # Label in the appropriate row and column
            gridLayout.addWidget(edit, i // 4, (i % 4) * 2 + 1)       # Edit in the adjacent column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print(f"Error: {e}")
