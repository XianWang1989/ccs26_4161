
import sys
from PyQt5 import QtWidgets, QtWebKitWidgets

class WebView(QtWebKitWidgets.QWebView):
    def __init__(self):
        super(WebView, self).__init__()
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, success):
        if success:
            # Execute JavaScript to get the DOM as a string
            self.page().mainFrame().evaluateJavaScript("""
                (function() {
                    return document.documentElement.outerHTML;
                })();
            """)

            # Handle the response in the callback
            self.page().mainFrame().setJavaScriptCallback(self.handle_dom)

    def handle_dom(self, dom_string):
        print("DOM content loaded:")
        print(dom_string)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    webview = WebView()
    webview.load("http://example.com")  # Replace with your URL
    webview.show()
    sys.exit(app.exec_())
