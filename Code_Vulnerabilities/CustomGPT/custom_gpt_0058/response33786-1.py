
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

def on_load_finished(success):
    if success:
        # Execute JavaScript to get the DOM
        view.page().runJavaScript("document.documentElement.outerHTML", handle_html)

def handle_html(html):
    print(html)  # This prints the entire HTML DOM structure

app = QApplication(sys.argv)

# Create a Web Engine View
view = QWebEngineView()
view.loadFinished.connect(on_load_finished)
view.setUrl(QUrl("http://www.example.com"))  # Load your desired URL
view.show()

sys.exit(app.exec_())
