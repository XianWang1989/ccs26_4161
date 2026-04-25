
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        labels = [
            "Author", "Title", 
            "Bodytext 1", "Bodytext 2", "Bodytext 3"
        ]

        for i, label in enumerate(labels):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # Label position
            if "Bodytext" in label:
                gridLayout.addWidget(QTextEdit(), i // 4, (i % 4) * 2 + 1)  # QTextEdit position
            else:
                gridLayout.addWidget(QLineEdit(), i // 4, (i % 4) * 2 + 1)  # QLineEdit position

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
