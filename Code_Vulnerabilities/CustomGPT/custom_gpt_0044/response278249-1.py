
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)
        self.setLayout(self.SetLayout())

    def SetLayout(self):
        gridLayout = QGridLayout(self)
        labels = ["Author", "Title", "Bodytext 1", "Bodytext 2", "Bodytext 3"]
        fields = [QLineEdit(), QLineEdit(), QTextEdit(), QTextEdit(), QTextEdit()]

        for i in range(len(labels)):
            label = QLabel(labels[i])
            field = fields[i]
            gridLayout.addWidget(label, i, 0)   # Label in the first column
            gridLayout.addWidget(field, i, 1)    # Field in the second column
            gridLayout.addWidget(QLabel(), i, 2) # Empty space for a third column
            gridLayout.addWidget(QLabel(), i, 3) # Empty space for a fourth column

        return gridLayout

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print("Error:", e)
