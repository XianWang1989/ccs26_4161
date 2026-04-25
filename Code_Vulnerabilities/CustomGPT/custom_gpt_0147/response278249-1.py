
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)  # Adjust size to fit more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)  # Use QGridLayout instead of QFormLayout

        # Define labels and inputs
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

        # Add widgets to the grid layout (you can adjust positions as needed)
        gridLayout.addWidget(labelAuthor, 0, 0)  # Row 0, Column 0
        gridLayout.addWidget(txtAuthor, 0, 1)     # Row 0, Column 1

        gridLayout.addWidget(labelTitle, 1, 0)    # Row 1, Column 0
        gridLayout.addWidget(txtTitle, 1, 1)       # Row 1, Column 1

        gridLayout.addWidget(labelBodytext1, 2, 0) # Row 2, Column 0
        gridLayout.addWidget(txtBodytext1, 2, 1)    # Row 2, Column 1

        gridLayout.addWidget(labelBodytext2, 3, 0) # Row 3, Column 0
        gridLayout.addWidget(txtBodytext2, 3, 1)    # Row 3, Column 1

        gridLayout.addWidget(labelBodytext3, 4, 0) # Row 4, Column 0
        gridLayout.addWidget(txtBodytext3, 4, 1)    # Row 4, Column 1

        # Optionally, add additional spacing or images if needed

        self.setLayout(gridLayout)

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
