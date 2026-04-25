
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.setLayout(self.createLayout())

    def createLayout(self):
        gridLayout = QGridLayout()

        # Create form labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add fields to the grid layout (4 columns)
        for i, (label, widget) in enumerate(fields):
            gridLayout.addWidget(QLabel(label), i // 4, 0)  # Label in column 0
            gridLayout.addWidget(widget, i // 4, 1 + (i % 4))  # Widgets in columns 1 to 4

        return gridLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
