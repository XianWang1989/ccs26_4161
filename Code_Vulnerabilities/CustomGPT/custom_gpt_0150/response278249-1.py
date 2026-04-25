
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Adding fields to the grid layout
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        for i, label in enumerate(labels):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # Label in column 0, 2, 4...
            if label.startswith("Bodytext"):
                gridLayout.addWidget(QTextEdit(), i // 4, (i % 4) * 2 + 1)  # TextEdit in column 1, 3, 5...
            else:
                gridLayout.addWidget(QLineEdit(), i // 4, (i % 4) * 2 + 1)

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
