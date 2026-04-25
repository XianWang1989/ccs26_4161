
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define the labels and their corresponding input fields
        form_elements = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Populate the grid layout (4 columns)
        for index, (label_text, widget) in enumerate(form_elements):
            row = index // 4  # Calculate the row number
            col = index % 4   # Calculate the column number
            gridLayout.addWidget(QLabel(label_text), row, col * 2)  # Label on each odd column
            gridLayout.addWidget(widget, row, col * 2 + 1)           # Input next to the label

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
