
import sys
from gi.repository import WebKit, Gtk

class MyWebView(Gtk.Window):
    def __init__(self):
        super(MyWebView, self).__init__()

        self.set_default_size(800, 600)
        self.webview = WebKit.WebView()

        # Connect to the 'load-finished' event
        self.webview.connect("load-finished", self.on_load_finished)

        self.webview.load_uri("http://example.com")  # Load your desired URL
        self.add(self.webview)
        self.show_all()

    def on_load_finished(self, webview, frame):
        # Evaluate JavaScript to get the DOM content
        script = "document.documentElement.outerHTML"
        webview.evaluate_script(script)

    def on_script_finished(self, webview, result, data):
        # This function handles the result of the script evaluation
        print("DOM Content:")
        print(result)  # This will contain the DOM as a string

if __name__ == "__main__":
    Gtk.init(sys.argv)
    MyWebView()
    Gtk.main()
