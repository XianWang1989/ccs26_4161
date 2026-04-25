
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 500, 200)  # Increased width for better layout

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Define labels and text fields
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        inputs = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        # Add fields to the grid layout
        for i, (label, input_field) in enumerate(zip(labels, inputs)):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # Label in even columns
            gridLayout.addWidget(input_field, i // 4, (i % 4) * 2 + 1)  # Input in odd columns

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
    except Exception:
        print(sys.exc_info()[1])
