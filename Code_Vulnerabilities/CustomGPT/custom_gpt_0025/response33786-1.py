
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            # Execute JavaScript to get the DOM content
            self.page().runJavaScript("document.documentElement.outerHTML", self.get_dom)

    def get_dom(self, html):
        print("DOM Loaded:")
        print(html)  # This will print the loaded HTML DOM

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MyWebView()
    view.load(QUrl("https://www.example.com"))
    view.show()
    sys.exit(app.exec_())
