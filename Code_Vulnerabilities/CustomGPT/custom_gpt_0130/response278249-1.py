
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 200)
        self.SetLayout()

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Add labels and corresponding fields to the grid layout
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        for i, label in enumerate(labels):
            gridLayout.addWidget(QLabel(label), i, 0)
            if "Bodytext" in label:
                gridLayout.addWidget(QTextEdit(), i, 1)
            else:
                gridLayout.addWidget(QLineEdit(), i, 1)

        # Adding extra columns for other interactions, if needed
        # You can also expand this to more columns
        gridLayout.addWidget(QLineEdit(), 0, 2)  # Example additional field
        gridLayout.addWidget(QLineEdit(), 1, 2)
        gridLayout.addWidget(QLineEdit(), 2, 2)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
