
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 200)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and line edits
        form_data = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Fill grid layout with labels and corresponding fields
        for i, (labelText, widget) in enumerate(form_data):
            label = QLabel(labelText)
            row = i // 4  # Calculate row number
            column = i % 4  # Calculate column number
            gridLayout.addWidget(label, row, column * 2)  # Label in 1st column
            gridLayout.addWidget(widget, row, column * 2 + 1)  # Widget in 2nd column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec_())
