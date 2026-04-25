
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Column Form")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and text fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        textEdits = [QLineEdit() for _ in range(2)] + [QTextEdit() for _ in range(3)]

        for i, label in enumerate(labels):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # label on even columns
            gridLayout.addWidget(textEdits[i], i // 4, (i % 4) * 2 + 1)  # text field on odd columns

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
