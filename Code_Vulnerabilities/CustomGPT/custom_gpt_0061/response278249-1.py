
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)  # Adjusted size for more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Add fields to the grid layout
        for i, (label, widget) in enumerate(fields):
            row = i // 4  # Determine the row (4 columns)
            col = i % 4   # Determine the column
            gridLayout.addWidget(QLabel(label), row, col * 2)   # Label in column 0, 2, 4, ...
            gridLayout.addWidget(widget, row, col * 2 + 1)       # Widget in column 1, 3, 5, ...

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
