
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)
        self.setLayout(self.setLayout())

    def setLayout(self):
        gridLayout = QGridLayout()

        # Create labels and input fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Add labels and fields to the grid
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)
            gridLayout.addWidget(input_field, i // 4, (i % 4) * 2 + 1)

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec())
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
