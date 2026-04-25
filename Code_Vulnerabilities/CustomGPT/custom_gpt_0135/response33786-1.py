
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class Browser(QtWidgets.QWidget):
    def __init__(self):
        super(Browser, self).__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.loadFinished.connect(self.on_load_finished)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)

        # Load a URL
        self.browser.setUrl(QtCore.QUrl("http://example.com"))

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to retrieve the DOM
            self.browser.page().runJavaScript("document.documentElement.outerHTML", self.handle_dom)

    def handle_dom(self, dom):
        print("DOM Loaded:")
        print(dom)  # Do something with the DOM, such as parsing or storing it

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Browser()
    window.show()
    app.exec_()
