
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)  # Adjusted size for multiple columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and inputs
        inputs = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add items to the grid layout
        for i, (label_text, input_widget) in enumerate(inputs):
            label = QLabel(label_text)
            gridLayout.addWidget(label, i // 4, (i % 4) * 2)  # Row, Column
            gridLayout.addWidget(input_widget, i // 4, (i % 4) * 2 + 1)  # Input next to the label

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
