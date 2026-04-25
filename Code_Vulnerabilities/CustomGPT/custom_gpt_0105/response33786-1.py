
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM content
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, dom):
        print(dom)  # Process or display the DOM content

if __name__ == "__main__":
    app = QApplication(sys.argv)
    webview = MyWebView()
    webview.load("http://www.example.com")  # Load your desired URL
    webview.show()
    sys.exit(app.exec_())
