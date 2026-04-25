
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class BrowserApp:
    def __init__(self):
        self.window = Gtk.Window(title="WebKit2 Example")
        self.webview = WebKit2.WebView()

        self.webview.connect("load-changed", self.on_load_changed)

        self.window.add(self.webview)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_default_size(800, 600)

        self.webview.load_uri("https://example.com")
        self.window.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.DOCUMENT_FINISHED:
            self.get_dom()

    def get_dom(self):
        script = "document.documentElement.outerHTML"
        self.webview.evaluate_javascript(script, self.on_dom_retrieved)

    def on_dom_retrieved(self, webview, result, error):
        if error:
            print("Error retrieving DOM:", error)
        else:
            print("DOM retrieved:", result.get_js_value())

if __name__ == "__main__":
    app = BrowserApp()
    Gtk.main()
