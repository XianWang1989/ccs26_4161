
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.loadFinished.connect(self.on_load_finished)
        self.setCentralWidget(self.browser)
        self.browser.setUrl("http://example.com")  # Replace with your URL

    def on_load_finished(self, result):
        if result:
            self.get_dom()

    def get_dom(self):
        self.browser.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, html):
        print(html)  # Output the HTML content of the DOM

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
