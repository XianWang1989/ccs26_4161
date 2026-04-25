
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def load_url(self, url):
        self.load(QUrl(url))

    def on_load_finished(self, ok):
        if ok:
            self.evaluateJavaScript("document.documentElement.outerHTML", self.on_js_evaluated)

    def on_js_evaluated(self, result):
        print("DOM content:", result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MyWebView()
    view.load_url("https://example.com")
    view.show()
    sys.exit(app.exec_())
