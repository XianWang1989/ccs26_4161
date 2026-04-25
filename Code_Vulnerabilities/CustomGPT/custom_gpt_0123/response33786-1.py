
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)

        # Connect the load finished signal
        self.browser.loadFinished.connect(self.on_load_finished)

        # Load a webpage
        self.browser.setUrl(QtCore.QUrl("http://example.com"))

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM
            self.browser.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, dom):
        # This function will receive the DOM as a string
        print(dom)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
