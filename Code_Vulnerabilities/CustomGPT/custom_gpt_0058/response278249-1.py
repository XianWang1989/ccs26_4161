
import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Title")
        self.setGeometry(300, 300, 600, 400)

    def SetLayout(self):
        mainLayout = QVBoxLayout(self)
        formLayout = QFormLayout()

        labelAuthor = QLabel("Author")
        txtAuthor = QLineEdit()
        labelTitle = QLabel("Title")
        txtTitle = QLineEdit()
        labelBodytext1 = QLabel("Bodytext 1")
        txtBodytext1 = QTextEdit()
        labelBodytext2 = QLabel("Bodytext 2")
        txtBodytext2 = QTextEdit()
        labelBodytext3 = QLabel("Bodytext 3")
        txtBodytext3 = QTextEdit()

        # Create individual layouts for every set of 4 fields
        layout1 = QHBoxLayout()
        layout1.addWidget(labelAuthor)
        layout1.addWidget(txtAuthor)

        layout2 = QHBoxLayout()
        layout2.addWidget(labelTitle)
        layout2.addWidget(txtTitle)

        layout3 = QHBoxLayout()
        layout3.addWidget(labelBodytext1)
        layout3.addWidget(txtBodytext1)

        layout4 = QHBoxLayout()
        layout4.addWidget(labelBodytext2)
        layout4.addWidget(txtBodytext2)

        layout5 = QHBoxLayout()
        layout5.addWidget(labelBodytext3)
        layout5.addWidget(txtBodytext3)

        # Adding the rows to the formLayout
        formLayout.addRow(layout1)
        formLayout.addRow(layout2)
        formLayout.addRow(layout3)
        formLayout.addRow(layout4)
        formLayout.addRow(layout5)

        mainLayout.addLayout(formLayout)
        self.setLayout(mainLayout)

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
