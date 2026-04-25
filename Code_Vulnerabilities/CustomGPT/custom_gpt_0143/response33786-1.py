
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class WebViewExample(Gtk.Window):
    def __init__(self):
        super().__init__(title="WebKit Example")
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)
        self.webview.load_uri("https://www.example.com")

        self.add(self.webview)
        self.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.FINISHED:
            self.get_dom_document()

    def get_dom_document(self):
        script = "document.documentElement.outerHTML"
        self.webview.evaluate_javascript(script, self.on_js_evaluated)

    def on_js_evaluated(self, webview, result, error):
        if error:
            print("Error:", error)
        else:
            print("DOM Content:", result.get_string())

if __name__ == "__main__":
    win = WebViewExample()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
