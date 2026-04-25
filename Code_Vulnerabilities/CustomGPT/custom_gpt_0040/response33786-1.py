
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, successful):
        if successful:
            self.page().runJavaScript('document.documentElement.outerHTML', self.on_get_dom)

    def on_get_dom(self, dom):
        print(dom)  # Here you can manipulate or use the DOM as needed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    webview = MyWebView()
    webview.load("http://example.com")
    webview.show()
    sys.exit(app.exec_())
