
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, result):
        if result:
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_html)

    def handle_html(self, html):
        print("DOM Loaded:")
        print(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    webview = MyWebView()

    # Load your URL here
    webview.setUrl('https://example.com')
    webview.resize(1024, 768)
    webview.show()

    sys.exit(app.exec_())
