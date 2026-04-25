
import sys
from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit, QGridLayout, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.SetLayout()

    def SetLayout(self):
        mainLayout = QVBoxLayout(self)
        gridLayout = QGridLayout()

        # Create labels and text fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit() for _ in range(2)] + [QTextEdit() for _ in range(3)]

        # Add labels and inputs to grid layout
        for i, label in enumerate(labels):
            gridLayout.addWidget(QLabel(label), i, 0)  # Column 0
            gridLayout.addWidget(inputs[i], i, 1)      # Column 1

        # Add additional columns as needed
        # Example for duplication or adding new elements
        gridLayout.addWidget(QLabel("Extra Field 1"), 0, 2)
        gridLayout.addWidget(QLineEdit(), 0, 3)
        gridLayout.addWidget(QLabel("Extra Field 2"), 1, 2)
        gridLayout.addWidget(QLineEdit(), 1, 3)

        mainLayout.addLayout(gridLayout)
        self.setLayout(mainLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("Error:", str(e))
