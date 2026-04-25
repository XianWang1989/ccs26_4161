
import sys
from PySide.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 175)  # Adjusted width for more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define your labels and inputs
        labels = [
            QLabel("Author"),
            QLabel("Title"),
            QLabel("Bodytext 1"),
            QLabel("Bodytext 2"),
            QLabel("Bodytext 3")
        ]

        inputs = [
            QLineEdit(),
            QLineEdit(),
            QTextEdit(),
            QTextEdit(),
            QTextEdit()
        ]

        # Add labels and inputs to the grid layout
        for i, label in enumerate(labels):
            row = i // 4  # Determine the row number
            col = i % 4   # Determine the column number
            gridLayout.addWidget(label, row, col * 2)  # Add the label
            gridLayout.addWidget(inputs[i], row, col * 2 + 1)  # Add the corresponding input

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
