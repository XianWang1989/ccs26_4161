
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyBrowser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.on_load_finished)
        self.browser.setUrl("http://example.com")

    def on_load_finished(self, ok):
        if ok:
            self.browser.page().runJavaScript("document.documentElement.innerHTML", self.get_dom)

    def get_dom(self, dom):
        print("DOM content:")
        print(dom)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyBrowser()
    window.show()
    sys.exit(app.exec_())
