
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 300)
        self.setLayout(self.SetLayout())

    def SetLayout(self):
        gridLayout = QGridLayout()

        # Field Labels
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Adding labels and inputs to the grid layout
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            row = i // 4
            col = i % 4
            gridLayout.addWidget(QLabel(label), row, col * 2)        # Label in the left column
            gridLayout.addWidget(input_field, row, col * 2 + 1)     # Input in the right column

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except Exception as e:
        print(f"Error: {e}")
