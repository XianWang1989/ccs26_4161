
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define widgets
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

        # Add widgets to the grid layout
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

        # You can adjust the spans if needed
        # For example, to combine columns for larger fields:
        # gridLayout.addWidget(txtBodytext1, row, column, rowSpan, columnSpan)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except Exception as e:
        print("Error:", e)
