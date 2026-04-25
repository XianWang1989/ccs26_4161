
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWebEngineView):
    def __init__(self):
        super(Browser, self).__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, finished):
        if finished:
            # Execute JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.get_dom)

    def get_dom(self, dom):
        print(dom)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.load("http://example.com")  # Replace with your URL
    browser.show()
    sys.exit(app.exec_())
