
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class Browser(Gtk.Window):
    def __init__(self):
        super(Browser, self).__init__()
        self.set_title("WebKit DOM Example")
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)
        self.add(self.webview)

        self.webview.load_uri("http://example.com")
        self.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMPLETE:
            # Page has loaded completely
            self.get_dom()

    def get_dom(self):
        # JavaScript code to get the DOM
        js_code = "document.documentElement.outerHTML;"
        self.webview.evaluate_javascript(js_code, self.on_dom_received)

    def on_dom_received(self, result, error):
        if error:
            print("Error evaluating JavaScript:", error)
        else:
            print("DOM:", result)

if __name__ == "__main__":
    win = Browser()
    Gtk.main()
