import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 300)
        self.setLayout(self.createLayout())

    def createLayout(self):
        gridLayout = QGridLayout()

        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add fields in label+input pairs, two per row (4 columns)
        for index, (label_text, widget) in enumerate(fields):
            row = index // 2
            col = (index % 2) * 2
            gridLayout.addWidget(QLabel(label_text), row, col)
            gridLayout.addWidget(widget, row, col + 1)

        return gridLayout

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("Error:", e)
