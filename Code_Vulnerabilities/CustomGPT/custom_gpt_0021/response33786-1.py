
import sys
from gi.repository import WebKit, Gtk

class WebViewDemo:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        self.webview.connect("load-finished", self.on_load_finished)
        self.window.add(self.webview)
        self.window.show_all()

        self.webview.load_uri("http://example.com")  # Load your desired URL

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM content
        webview.execute_script("document.documentElement.outerHTML", self.on_dom_received)

    def on_dom_received(self, result, frame):
        print("DOM content:")
        print(result)

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    demo = WebViewDemo()
    demo.run()
