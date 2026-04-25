
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 200)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and text inputs
        labels = [
            QLabel("Author"), QLabel("Title"), QLabel("Bodytext 1"),
            QLabel("Bodytext 2"), QLabel("Bodytext 3")
        ]
        inputs = [
            QLineEdit(), QLineEdit(),
            QTextEdit(), QTextEdit(), QTextEdit()
        ]

        # Add them to the grid layout
        for i in range(len(labels)):
            gridLayout.addWidget(labels[i], i // 4, (i % 4) * 2)
            gridLayout.addWidget(inputs[i], i // 4, (i % 4) * 2 + 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
