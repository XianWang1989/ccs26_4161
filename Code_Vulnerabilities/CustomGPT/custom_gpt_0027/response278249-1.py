
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.setLayout(self.SetLayout())

    def SetLayout(self):
        gridLayout = QGridLayout()

        # Creating labels and text input fields
        controls = [
            (QLabel("Author"), QLineEdit()),
            (QLabel("Title"), QLineEdit()),
            (QLabel("Bodytext 1"), QTextEdit()),
            (QLabel("Bodytext 2"), QTextEdit()),
            (QLabel("Bodytext 3"), QTextEdit())
        ]

        # Placing widgets into the grid
        for i, (label, control) in enumerate(controls):
            gridLayout.addWidget(label, i // 4, (i % 4) * 2)  # Labels in one column
            gridLayout.addWidget(control, i // 4, (i % 4) * 2 + 1)  # Controls in next column

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
