
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk

class Browser(Gtk.Window):
    def __init__(self):
        super().__init__(title="WebKit Example")
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)
        self.webview.load_uri("https://example.com")  # Load your URL here

        self.add(self.webview)
        self.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.FINISHED:
            self.get_dom_document()

    def get_dom_document(self):
        # Execute JavaScript to get the DOM
        self.webview.evaluate_javascript("document.documentElement.outerHTML", self.on_result)

    def on_result(self, result):
        print("DOM Document:")
        print(result.get_js_value())

win = Browser()
Gtk.main()
