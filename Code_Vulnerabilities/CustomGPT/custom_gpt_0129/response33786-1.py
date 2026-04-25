
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class MyWebView:
    def __init__(self):
        self.window = Gtk.Window(title="WebKit Example")
        self.webview = WebKit2.WebView()

        # Connect to the load finished signal
        self.webview.connect("load-changed", self.on_load_changed)

        # Load a webpage
        self.webview.load_uri("http://example.com")

        self.window.add(self.webview)
        self.window.set_default_size(800, 600)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def on_load_changed(self, webview, load_event):
        # Check if the load event is finished
        if load_event == WebKit2.LoadEvent.FINISHED:
            # Execute JavaScript to get the DOM content
            self.webview.evaluate_javascript("document.documentElement.outerHTML", self.dom_callback)

    def dom_callback(self, webview, result, *data):
        if result.get_is_string():
            dom_content = result.get_string()
            print("DOM Content Loaded:")
            print(dom_content)

if __name__ == "__main__":
    MyWebView()
    Gtk.main()
