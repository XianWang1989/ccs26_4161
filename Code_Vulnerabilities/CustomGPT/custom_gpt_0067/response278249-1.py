
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 800, 400)  # Adjust width for more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add fields in a 4-column layout
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        for index, (label, field) in enumerate(fields):
            row = index // 4  # Determine the row
            col = index % 4   # Determine the column
            gridLayout.addWidget(QLabel(label), row, col * 2)  # Label on even columns
            gridLayout.addWidget(field, row, col * 2 + 1)      # Field on odd columns

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
