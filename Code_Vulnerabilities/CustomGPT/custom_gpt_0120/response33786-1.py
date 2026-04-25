
import sys
from gi.repository import WebKit, Gtk

class WebViewApp(Gtk.Window):
    def __init__(self):
        super(WebViewApp, self).__init__()

        self.set_title("WebKit DOM Example")
        self.set_default_size(800, 600)

        self.webview = WebKit.WebView()
        self.webview.connect("load-finished", self.on_load_finished)
        self.webview.load_uri("http://example.com")

        self.add(self.webview)
        self.show_all()

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        js_code = "document.documentElement.outerHTML"
        frame.evaluate_script(js_code)

    def on_script_finished(self, widget, result):
        print("DOM:", result)  # Handle the result as needed

if __name__ == "__main__":
    Gtk.main()
