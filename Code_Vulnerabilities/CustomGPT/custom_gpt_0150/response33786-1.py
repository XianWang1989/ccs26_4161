
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_result)

    def handle_result(self, result):
        print("DOM Loaded:\n", result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    webview = MyWebView()
    webview.load("https://example.com")
    webview.show()
    sys.exit(app.exec_())
