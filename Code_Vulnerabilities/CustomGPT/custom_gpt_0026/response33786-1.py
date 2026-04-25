
import gi
gi.require_version('WebKit', '4.0')
from gi.repository import Gtk, WebKit

class WebViewExample:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        # Connect to the load-finished signal
        self.webview.connect("load-finished", self.on_load_finished)
        self.window.add(self.webview)
        self.window.set_default_size(800, 600)
        self.window.show_all()

        # Load a URL
        self.webview.load_uri("https://www.example.com")

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        frame.evaluate("document.documentElement.outerHTML", self.get_dom)

    def get_dom(self, result):
        # This callback is called with the DOM as a string
        print(result)  # Here you can process or store the DOM

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = WebViewExample()
    app.run()
