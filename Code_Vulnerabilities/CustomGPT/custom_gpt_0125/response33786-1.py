
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class WebViewExample(Gtk.Window):
    def __init__(self):
        super(WebViewExample, self).__init__()
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)

        self.add(self.webview)
        self.webview.load_uri("https://example.com")

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITS:
            # Execute JavaScript to get the DOM
            self.webview.evaluate_javascript("document.documentElement.outerHTML", self.javascript_callback)

    def javascript_callback(self, webview, result, error):
        if error is None:
            dom_html = result.get_string()  # Get the resulting HTML
            print(dom_html)  # Output the HTML content
        else:
            print("Error running JavaScript:", error)

win = WebViewExample()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
