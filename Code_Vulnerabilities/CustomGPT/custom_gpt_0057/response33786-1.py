
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QObject, pyqtSignal

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            self.page().toHtml(self.handle_html)

    def handle_html(self, html):
        print("DOM Loaded:")
        print(html)

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    web_view = WebView()
    window.setCentralWidget(web_view)
    window.resize(800, 600)
    web_view.load(QUrl("http://example.com"))  # Replace with your URL
    window.show()
    app.exec_()
