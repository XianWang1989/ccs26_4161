
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, dom):
        print("DOM Loaded:")
        print(dom)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web_view = WebView()
    web_view.load("https://example.com")  # Load the desired webpage
    web_view.show()
    sys.exit(app.exec_())
