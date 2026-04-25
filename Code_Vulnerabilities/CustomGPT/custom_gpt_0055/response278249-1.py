
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add to grid layout
        for index, (label, widget) in enumerate(fields):
            row = index // 4  # Each row has 4 columns
            column = index % 4
            gridLayout.addWidget(QLabel(label), row, column * 2)  # Label on left
            gridLayout.addWidget(widget, row, column * 2 + 1)      # Widget on right

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
