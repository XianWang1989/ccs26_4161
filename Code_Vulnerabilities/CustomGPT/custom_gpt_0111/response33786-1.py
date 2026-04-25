
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.loadFinished.connect(self.on_load_finished)
        self.setCentralWidget(self.browser)
        self.browser.setUrl("https://example.com")

    def on_load_finished(self, ok):
        if ok:
            # Execute JavaScript to get the DOM
            self.browser.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, dom):
        print(dom)  # Print the DOM or process it as needed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
