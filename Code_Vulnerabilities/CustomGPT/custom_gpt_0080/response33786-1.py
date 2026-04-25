
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)
        self.load("https://www.example.com")

    def on_load_finished(self, success):
        if success:
            self.page().runJavaScript("document.documentElement.innerHTML", self.handle_dom)

    def handle_dom(self, dom):
        print("DOM content:")
        print(dom)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    webview = WebView()
    webview.show()
    sys.exit(app.exec_())
