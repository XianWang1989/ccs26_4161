
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 200)

    def set_layout(self):
        grid_layout = QGridLayout(self)

        # Create labels and text fields
        form_elements = [
            ("Author", QLineEdit()),
            ("Title", QLineEdit()),
            ("Bodytext 1", QTextEdit()),
            ("Bodytext 2", QTextEdit()),
            ("Bodytext 3", QTextEdit())
        ]

        # Add elements to the grid layout
        for index, (label_text, widget) in enumerate(form_elements):
            label = QLabel(label_text)
            grid_layout.addWidget(label, index // 4, (index % 4) * 2)
            grid_layout.addWidget(widget, index // 4, (index % 4) * 2 + 1)

        self.setLayout(grid_layout)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.set_layout()
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error: {e}")
