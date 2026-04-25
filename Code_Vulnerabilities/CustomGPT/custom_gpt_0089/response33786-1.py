
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, html):
        print("DOM Loaded:")
        print(html)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    web_view = MyWebView()
    web_view.load("https://example.com")  # Replace with your URL
    web_view.show()
    sys.exit(app.exec_())
