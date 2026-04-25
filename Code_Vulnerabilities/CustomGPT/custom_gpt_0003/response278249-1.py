
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 300)  # Increased width for better layout visibility

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define the labels and corresponding inputs
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Place the fields in a grid layout (4 columns)
        for i, (label, widget) in enumerate(fields):
            row = i // 4  # Determine the row number
            col = i % 4   # Determine the column number
            gridLayout.addWidget(QLabel(label), row, col * 2)  # Label in the 1st column of the cell
            gridLayout.addWidget(widget, row, col * 2 + 1)      # Widget in the 2nd column of the cell

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
