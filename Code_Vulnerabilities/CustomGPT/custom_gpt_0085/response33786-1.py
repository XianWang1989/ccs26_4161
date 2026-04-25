
from PyQt5 import QtWidgets, QtWebEngineWidgets
import sys

class Browser(QtWidgets.QWidget):
    def __init__(self):
        super(Browser, self).__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.browser.loadFinished.connect(self.on_load_finished)
        self.browser.setUrl('https://example.com')  # Load your desired URL

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)
        self.setWindowTitle('WebKit DOM Example')

    def on_load_finished(self, ok):
        if ok:
            # Execute JavaScript to retrieve the DOM
            self.browser.page().runJavaScript('document.documentElement.outerHTML', self.handle_dom)

    def handle_dom(self, html):
        print(html)  # Print or process the DOM as needed

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
