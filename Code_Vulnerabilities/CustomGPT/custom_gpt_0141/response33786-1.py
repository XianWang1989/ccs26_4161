
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class MyWebView(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="WebKit Example")
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)
        self.webview.load_uri("https://example.com")

        self.add(self.webview)
        self.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITTED:
            # Wait for the page to be fully loaded
            webview.run_javascript("document.documentElement.outerHTML", None, self.on_javascript_finished, None)

    def on_javascript_finished(self, result, user_data):
        # Get the DOM as a string
        dom_document = result.get_data() if result else "Failed to get DOM"
        print("DOM Document:")
        print(dom_document)

if __name__ == "__main__":
    win = MyWebView()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
