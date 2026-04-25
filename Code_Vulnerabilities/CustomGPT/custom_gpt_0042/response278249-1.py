
import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and line edits
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        textEdits = [QLineEdit() for _ in range(2)] + [QTextEdit() for _ in range(3)]

        # Add items to the grid layout
        for index, (label, textEdit) in enumerate(zip(labels, textEdits)):
            gridLayout.addWidget(QLabel(label), index // 4, (index % 4) * 2)  # Label
            gridLayout.addWidget(textEdit, index // 4, (index % 4) * 2 + 1)   # Text Edit

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
