
import sys
from PySide.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)  # Adjust size for 4 columns

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # List of labels and corresponding widgets
        fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit()),
        ]

        # Loop to add labels and widgets to the grid layout
        for index, (label_text, widget) in enumerate(fields):
            label = QLabel(label_text)
            gridLayout.addWidget(label, index // 4, (index % 4) * 2)  # Row, Column
            gridLayout.addWidget(widget, index // 4, (index % 4) * 2 + 1)  # Row, Column

        self.setLayout(gridLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        sys.exit(myApp.exec_())
    except Exception as e:
        print("Error:", e)
