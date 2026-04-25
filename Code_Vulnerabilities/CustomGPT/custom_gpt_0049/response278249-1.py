
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Defining labels and text fields
        labels_and_fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Adding fields to the grid layout (4 columns)
        for index, (label_text, field) in enumerate(labels_and_fields):
            row = index // 4  # Determine the row number based on the index
            column = index % 4  # Determine the column number based on the index
            gridLayout.addWidget(QLabel(label_text), row, column * 2)  # Label in even columns
            gridLayout.addWidget(field, row, column * 2 + 1)  # Field in odd columns

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
