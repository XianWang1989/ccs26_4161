
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define the labels and fields
        labels_and_fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add labels and fields to the grid layout
        row = 0
        column = 0
        for label_text, field in labels_and_fields:
            label = QLabel(label_text)
            gridLayout.addWidget(label, row, column)
            gridLayout.addWidget(field, row + 1, column)
            column += 1

            # Move to the next row when reaching 4 columns
            if column >= 4:
                column = 0
                row += 2  # Move to the next row (2 rows for each field)

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
