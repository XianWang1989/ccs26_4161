
import sys
from gi.repository import WebKit, Gtk

class WebViewExample(Gtk.Window):
    def __init__(self):
        super(WebViewExample, self).__init__()
        self.set_title("WebKit DOM Example")
        self.set_size_request(800, 600)

        self.webview = WebKit.WebView()
        self.webview.load_uri("https://example.com")
        self.webview.connect("load-finished", self.on_load_finished)

        self.add(self.webview)
        self.show_all()

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM content
        script = "document.documentElement.outerHTML"

        # Evaluate the JS script
        webview.evaluate(script)

        # Get the result of the script
        result = webview.get_main_frame().get_execution_context().evaluate(script)
        print("DOM content:", result)

if __name__ == "__main__":
    Gtk.init(sys.argv)
    window = WebViewExample()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()
