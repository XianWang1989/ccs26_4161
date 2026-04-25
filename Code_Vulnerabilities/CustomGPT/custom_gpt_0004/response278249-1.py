
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 400, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)

        # Creating labels and text fields
        labels_text_fields = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Adding them to the grid layout
        for i, (label, text_field) in enumerate(labels_text_fields):
            gridLayout.addWidget(QLabel(label), i // 4, (i % 4) * 2)  # Place label
            gridLayout.addWidget(text_field, i // 4, (i % 4) * 2 + 1)  # Place text field

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.SetLayout()
    mainWindow.show()
    sys.exit(app.exec())
