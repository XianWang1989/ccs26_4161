
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class WebViewExample:
    def __init__(self):
        self.window = Gtk.Window(title="WebKit Example")
        self.webview = WebKit2.WebView()

        # Connect to the load finished event
        self.webview.connect("load-changed", self.on_load_changed)

        # Load a URL
        self.webview.load_uri("https://www.example.com")
        self.window.add(self.webview)
        self.window.set_default_size(800, 600)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITTED:
            # Execute JavaScript to get the entire DOM
            self.webview.run_javascript("document.documentElement.outerHTML;", None, self.on_js_finished, None)

    def on_js_finished(self, webview, result, user_data):
        if result:
            dom = result.get_js_value()  # Get the JavaScript value
            print(f"DOM: {dom}")

if __name__ == "__main__":
    WebViewExample()
    Gtk.main()
