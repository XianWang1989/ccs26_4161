
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        fields = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        for i, (label, field) in enumerate(zip(labels, fields)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)
            gridLayout.addWidget(field, i // 4, (i % 4) * 2 + 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception:
        print(sys.exc_info()[1])
