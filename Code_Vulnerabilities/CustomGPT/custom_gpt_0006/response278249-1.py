
import sys
from PySide.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Labels and fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Adding labels and fields to the grid layout
        for index, (label, field) in enumerate(fields):
            row = index // 4   # Determine the row
            col = index % 4    # Determine the column
            gridLayout.addWidget(QLabel(label), row, col)
            gridLayout.addWidget(field, row, col + 1)  # Place the field next to the label

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
    except Exception as e:
        print("An error occurred:", e)
