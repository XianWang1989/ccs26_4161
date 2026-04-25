
import sys
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 250)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Labels and input fields
        labelAuthor = QLabel("Author")
        txtAuthor = QLineEdit()
        labelTitle = QLabel("Title")
        txtTitle = QLineEdit()
        labelBodytext1 = QLabel("Bodytext 1")
        txtBodytext1 = QTextEdit()
        labelBodytext2 = QLabel("Bodytext 2")
        txtBodytext2 = QTextEdit()
        labelBodytext3 = QLabel("Bodytext 3")
        txtBodytext3 = QTextEdit()

        # Adding labels and input fields to the grid layout
        gridLayout.addWidget(labelAuthor, 0, 0)
        gridLayout.addWidget(txtAuthor, 0, 1)
        gridLayout.addWidget(labelTitle, 1, 0)
        gridLayout.addWidget(txtTitle, 1, 1)
        gridLayout.addWidget(labelBodytext1, 2, 0)
        gridLayout.addWidget(txtBodytext1, 2, 1)
        gridLayout.addWidget(labelBodytext2, 3, 0)
        gridLayout.addWidget(txtBodytext2, 3, 1)
        gridLayout.addWidget(labelBodytext3, 4, 0)
        gridLayout.addWidget(txtBodytext3, 4, 1)

        # Optionally, add more columns
        # Example: Another column for additional details
        gridLayout.addWidget(QLabel("Additional Info 1"), 0, 2)
        gridLayout.addWidget(QLineEdit(), 0, 3)
        gridLayout.addWidget(QLabel("Additional Info 2"), 1, 2)
        gridLayout.addWidget(QLineEdit(), 1, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec()
        sys.exit(0)
    except Exception as e:
        print("Error:", e)
