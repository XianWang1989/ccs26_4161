
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.process_dom)

    def process_dom(self, dom):
        print(dom)  # Here you can process the DOM as needed

if __name__ == "__main__":
    app = QApplication([])
    web_view = MyWebView()
    web_view.load(QUrl("https://example.com"))  # Replace with your desired URL
    web_view.show()
    app.exec_()
