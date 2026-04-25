
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        text_inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        for i, (label, text_input) in enumerate(zip(labels, text_inputs)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # Place label
            gridLayout.addWidget(text_input, i // 4, (i % 4) * 2 + 1)  # Place input next to label

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
