
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            self.page().runJavaScript("document.documentElement.outerHTML", self.get_dom)

    def get_dom(self, dom):
        print(dom)  # Here you'll have the complete DOM as a string

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyWebView()
    view.setUrl("https://example.com")  # Replace with your URL
    view.show()
    sys.exit(app.exec_())
