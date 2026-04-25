
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QObject, pyqtSlot

class WebEnginePage(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    @pyqtSlot(bool)
    def on_load_finished(self, success):
        if success:
            self.page().runJavaScript("document.documentElement.outerHTML", self.handle_html)

    def handle_html(self, html):
        print(html)  # You can process the HTML here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    webview = WebEnginePage()
    webview.setUrl("https://example.com")
    webview.show()
    sys.exit(app.exec_())
