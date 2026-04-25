
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
            self.page().runJavaScript("document.documentElement.outerHTML", self.process_dom)

    def process_dom(self, dom):
        print("DOM loaded:")
        print(dom)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    webview = WebView()
    webview.load("https://example.com")  # Change to your desired URL
    webview.show()
    sys.exit(app.exec_())
