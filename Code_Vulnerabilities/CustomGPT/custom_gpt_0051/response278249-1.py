
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 300)
        self.setLayout()

    def setLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and inputs
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Add labels and inputs to the grid layout
        for i, (label, input_widget) in enumerate(zip(labels, inputs)):
            gridLayout.addWidget(QLabel(label), i, 0)
            gridLayout.addWidget(input_widget, i, 1)

        # Adjust column spans (optional)
        for i in range(len(labels)):
            gridLayout.addWidget(QLabel(labels[i]), i, 0)
            input_widget = inputs[i]
            gridLayout.addWidget(input_widget, i, 1)

            if i % 4 == 0:  # Example: start new row after 4 columns
                gridLayout.addWidget(QLabel(""), i, 2)  # Placeholder for empty space
                gridLayout.addWidget(QLabel(""), i, 3)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print("Error:", e)
