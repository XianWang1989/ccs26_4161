
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add labels and input fields to the grid
        gridLayout.addWidget(QLabel("Author"), 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        gridLayout.addWidget(QLabel("Title"), 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1)

        gridLayout.addWidget(QLabel("Bodytext 1"), 2, 0)
        gridLayout.addWidget(QTextEdit(), 2, 1)

        gridLayout.addWidget(QLabel("Bodytext 2"), 3, 0)
        gridLayout.addWidget(QTextEdit(), 3, 1)

        gridLayout.addWidget(QLabel("Bodytext 3"), 4, 0)
        gridLayout.addWidget(QTextEdit(), 4, 1)

        # Add more fields to fill out four columns
        for i in range(5):  # Example: Adding extra fields
            gridLayout.addWidget(QLabel(f"Extra Field {i+1}"), i, 2)
            gridLayout.addWidget(QLineEdit(), i, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print(f"Error: {e}")
