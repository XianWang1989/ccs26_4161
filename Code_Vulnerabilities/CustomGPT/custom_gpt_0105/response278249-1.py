
import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and input fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        fields = [QLineEdit() for _ in range(2)] + [QTextEdit() for _ in range(3)]

        # Add the fields to the grid layout
        for i, (label, field) in enumerate(zip(labels, fields)):
            row = i // 4
            column = i % 4
            gridLayout.addWidget(QLabel(label), row, column * 2)
            gridLayout.addWidget(field, row, column * 2 + 1)

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
