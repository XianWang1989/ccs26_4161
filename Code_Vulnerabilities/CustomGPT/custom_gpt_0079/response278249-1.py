
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        fields = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Add fields to the grid layout
        for i, (label, field) in enumerate(zip(labels, fields)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)   # Label in the first column
            gridLayout.addWidget(field, i // 4, (i % 4) * 2 + 1)      # Field in the second column

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
