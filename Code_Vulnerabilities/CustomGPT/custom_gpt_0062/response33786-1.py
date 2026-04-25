
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl

class MyWebView(QWebView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM as a string
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, dom):
        if dom:
            print("DOM Loaded Successfully:")
            print(dom)
        else:
            print("Failed to retrieve DOM.")

if __name__ == '__main__':
    app = QApplication([])
    webview = MyWebView()
    webview.setUrl(QUrl("http://example.com"))
    webview.show()
    app.exec_()
