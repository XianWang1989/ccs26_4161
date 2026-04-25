
import sys
from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)  # Adjust width for multiple columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Populate the grid with form fields
        for i, (label, widget) in enumerate(fields):
            row = i // 4  # Determine the row number
            col = i % 4   # Determine the column number
            gridLayout.addWidget(QLabel(label), row, col * 2)  # Label
            gridLayout.addWidget(widget, row, col * 2 + 1)      # Widget

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
