
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 175)  # Adjusted width for 4 columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Adding labels and fields to the grid layout
        gridLayout.addWidget(QLabel("Author"), 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1, 1, 2)  # Span 2 columns for Author
        gridLayout.addWidget(QLabel("Title"), 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1, 1, 2)  # Span 2 columns for Title
        gridLayout.addWidget(QLabel("Bodytext 1"), 2, 0)
        gridLayout.addWidget(QTextEdit(), 2, 1, 1, 2)  # Span 2 columns for Bodytext 1
        gridLayout.addWidget(QLabel("Bodytext 2"), 3, 0)
        gridLayout.addWidget(QTextEdit(), 3, 1, 1, 2)  # Span 2 columns for Bodytext 2
        gridLayout.addWidget(QLabel("Bodytext 3"), 4, 0)
        gridLayout.addWidget(QTextEdit(), 4, 1, 1, 2)  # Span 2 columns for Bodytext 3

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
