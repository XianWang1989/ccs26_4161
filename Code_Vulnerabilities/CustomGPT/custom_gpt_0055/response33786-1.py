
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.loadFinished.connect(self.on_load_finished)
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl("http://example.com"))
        self.show()

    def on_load_finished(self, success):
        if success:
            self.browser.page().toHtml(self.handle_html)

    def handle_html(self, result):
        print("DOM Content:")
        print(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    sys.exit(app.exec_())
