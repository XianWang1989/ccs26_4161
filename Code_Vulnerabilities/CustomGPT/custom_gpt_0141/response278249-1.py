
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)  # Adjusted size for 4-column layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define your labels and text fields
        labels = [
            "Author", "Title", 
            "Bodytext 1", "Bodytext 2", "Bodytext 3"
        ]

        text_fields = [
            QLineEdit(), QLineEdit(),
            QTextEdit(), QTextEdit(), QTextEdit()
        ]

        # Add labels and fields to the grid layout
        for i, (label, text_field) in enumerate(zip(labels, text_fields)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)           # Place label in column 0, 2, 4...
            gridLayout.addWidget(text_field, i // 4, (i % 4) * 2 + 1)        # Place text field in column 1, 3, 5...

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
    except Exception as e:
        print("An error occurred:", str(e))
