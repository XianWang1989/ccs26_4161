
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def javaScriptConsoleMessage(self, level, msg, lineNumber, sourceID):
        print(f"Console: {msg} ({lineNumber})")

class WebEngineWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.on_load_finished)
        self.browser.setHtml('<html><body><h1>Hello, World!</h1></body></html>')

    def on_load_finished(self, success):
        if success:
            self.browser.page().runJavaScript("document.documentElement.outerHTML", self.handle_html)

    def handle_html(self, html):
        print(html)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebEngineWindow()
    window.show()
    sys.exit(app.exec_())
