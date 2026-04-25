
import sys
from PySide.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

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

        # Add elements to grid layout (4 columns)
        gridLayout.addWidget(labelAuthor, 0, 0)
        gridLayout.addWidget(txtAuthor, 0, 1)
        gridLayout.addWidget(labelTitle, 0, 2)
        gridLayout.addWidget(txtTitle, 0, 3)

        gridLayout.addWidget(labelBodytext1, 1, 0)
        gridLayout.addWidget(txtBodytext1, 1, 1)
        gridLayout.addWidget(labelBodytext2, 1, 2)
        gridLayout.addWidget(txtBodytext2, 1, 3)

        gridLayout.addWidget(labelBodytext3, 2, 0)
        gridLayout.addWidget(txtBodytext3, 2, 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
    except SystemExit:
        print("Closing Window...")
    except Exception as e:
        print("An error occurred:", e)
