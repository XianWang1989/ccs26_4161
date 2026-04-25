
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MyWebView(QWebEngineView):
    def __init__(self):
        super(MyWebView, self).__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Use JavaScript to get the DOM
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_html)

    def handle_html(self, html):
        print("HTML Document after page load:")
        print(html)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    web = MyWebView()
    web.setUrl(QUrl('http://www.example.com'))
    web.show()
    sys.exit(app.exec_())
