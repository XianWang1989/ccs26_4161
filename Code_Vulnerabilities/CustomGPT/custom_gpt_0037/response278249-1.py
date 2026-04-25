
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)  # Adjusted size for better layout

        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and inputs
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Add labels and inputs to the grid layout
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)     # Place label
            gridLayout.addWidget(input_field, i // 4, (i % 4) * 2 + 1)  # Place corresponding input

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
