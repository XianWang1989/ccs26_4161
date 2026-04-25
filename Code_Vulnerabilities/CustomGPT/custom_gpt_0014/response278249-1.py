
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)
        self.setLayout(self.setLayout())

    def setLayout(self):
        gridLayout = QGridLayout()

        # Define your labels and text fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add fields to the grid layout
        for i, (label_text, widget) in enumerate(fields):
            label = QLabel(label_text)
            gridLayout.addWidget(label, i // 4, (i % 4) * 2)  # Label in even columns
            gridLayout.addWidget(widget, i // 4, (i % 4) * 2 + 1)  # Widget in odd columns

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("Error:", e)
