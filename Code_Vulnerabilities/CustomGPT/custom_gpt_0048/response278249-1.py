
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)
        self.setLayout(self.createLayout())

    def createLayout(self):
        gridLayout = QGridLayout()

        # Adding labels and input fields in a 4-column layout
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        for i, (label_text, widget) in enumerate(fields):
            label = QLabel(label_text)
            row = i // 4  # Determine the row
            col = i % 4   # Determine the column
            gridLayout.addWidget(label, row, col * 2)    # Label occupies column 0, 2
            gridLayout.addWidget(widget, row, col * 2 + 1)  # Input field occupies column 1, 3

        return gridLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
