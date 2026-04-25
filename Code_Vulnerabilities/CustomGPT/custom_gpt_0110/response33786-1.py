
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.on_html_received)

    def on_html_received(self, html):
        print(html)  # Do something with the HTML

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.load('http://example.com')  # Replace with your URL
    browser.show()
    sys.exit(app.exec_())
