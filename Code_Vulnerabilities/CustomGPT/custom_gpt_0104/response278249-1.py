
import sys
from PySide.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)  # Adjusted window size for better layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define the labels and text fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Loop to add fields to the grid layout
        for i, (labelText, widget) in enumerate(fields):
            label = QLabel(labelText)
            row_position = i // 4  # Determine the row position
            column_position = i % 4  # Determine the column position
            gridLayout.addWidget(label, row_position, column_position * 2)  # Add label
            gridLayout.addWidget(widget, row_position, column_position * 2 + 1)  # Add input widget

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
