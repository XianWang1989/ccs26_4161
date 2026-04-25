
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            # Execute JavaScript to get the DOM content
            self.page().runJavaScript('document.documentElement.outerHTML', self.handle_dom)

    def handle_dom(self, dom_content):
        print(dom_content)  # Here you can process the DOM as needed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    webview = MyWebView()
    webview.load(QUrl('http://example.com'))  # Change to your desired URL
    webview.show()
    sys.exit(app.exec_())
