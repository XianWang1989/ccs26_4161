
import sys
from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)  # Adjusted width and height

    def SetLayout(self):
        mainLayout = QVBoxLayout(self)

        # Create a form layout
        formLayout = QFormLayout()

        # Create labels and input fields
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

        # Add rows to the form layout
        formLayout.addRow(labelAuthor, txtAuthor)
        formLayout.addRow(labelTitle, txtTitle)
        formLayout.addRow(labelBodytext1, txtBodytext1)
        formLayout.addRow(labelBodytext2, txtBodytext2)
        formLayout.addRow(labelBodytext3, txtBodytext3)

        # Create a grid layout for multiple columns
        gridLayout = QVBoxLayout()
        gridLayout.addLayout(formLayout)

        # Set the main layout
        mainLayout.addLayout(gridLayout)
        self.setLayout(mainLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
