
import sys
from PySide2.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 200)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Adding fields to the grid
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        textEdits = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        for i, (label, txtEdit) in enumerate(zip(labels, textEdits)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)
            gridLayout.addWidget(txtEdit, i // 4, (i % 4) * 2 + 1)

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
