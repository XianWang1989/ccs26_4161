
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load_finished(success):
    if success:
        print("Page loaded successfully.")
        # Execute JavaScript to get the DOM
        view.page().runJavaScript("document.documentElement.outerHTML", handle_dom)
    else:
        print("Failed to load the page.")

def handle_dom(dom):
    print("DOM Content:")
    print(dom)

app = QApplication([])
view = QWebEngineView()
view.loadFinished.connect(load_finished)
view.setUrl(QUrl("https://example.com"))  # Replace with your desired URL
view.show()
app.exec_()
