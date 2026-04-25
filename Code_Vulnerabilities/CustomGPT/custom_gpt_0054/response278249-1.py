
import sys
from PySide2.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 175)  # Adjusted width for more columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define your labels and text fields
        labels = [
            "Author", "Title", 
            "Bodytext 1", "Bodytext 2", "Bodytext 3"
        ]
        text_edits = [
            QLineEdit(), QLineEdit(),
            QTextEdit(), QTextEdit(), QTextEdit()
        ]

        # Place the labels and text fields in the grid layout
        for i, label in enumerate(labels):
            gridLayout.addWidget(QLabel(label), i // 4, i % 4)  # Row i//4, Column i%4
            gridLayout.addWidget(text_edits[i], i // 4, (i % 4) + 1)  # TextEdit to the right of the label

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
