
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            # Execute JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_result)

    def handle_result(self, html):
        print("DOM after page load:")
        print(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = WebView()
    view.load("http://example.com")
    view.show()
    sys.exit(app.exec_())
