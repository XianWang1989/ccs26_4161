
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 550, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and input fields
        labels = [QLabel("Author"), QLabel("Title"), QLabel("Bodytext 1"), QLabel("Bodytext 2"), QLabel("Bodytext 3")]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Add to grid layout (4 columns)
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            row = i // 4  # Determine the row
            col = i % 4   # Determine the column
            gridLayout.addWidget(label, row, col)
            gridLayout.addWidget(input_field, row + 1, col)  # Place input below the label

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print("Error:", e)
