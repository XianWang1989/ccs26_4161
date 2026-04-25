
import sys
from PySide.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Create labels and text fields
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Place fields in the grid layout
        for i, (label, widget) in enumerate(fields):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)   # Labels in the first column
            gridLayout.addWidget(widget, i // 4, (i % 4) * 2 + 1)      # Widgets in the second column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
