
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyBrowser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def load_url(self, url):
        self.load(url)

    def on_load_finished(self, success):
        if success:
            self.page().toHtml(self.get_dom)

    def get_dom(self, html):
        print("DOM loaded:")
        print(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = MyBrowser()
    browser.load_url("https://example.com")
    browser.show()
    sys.exit(app.exec_())
