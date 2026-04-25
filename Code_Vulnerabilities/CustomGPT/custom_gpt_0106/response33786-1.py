
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class WebViewExample:
    def __init__(self):
        self.window = Gtk.Window(title="WebKit Example")
        self.webview = WebKit2.WebView()

        # Connect to the load-finished signal
        self.webview.connect("load-changed", self.on_load_changed)

        # Load a webpage
        self.webview.load_uri("https://www.example.com")

        self.window.add(self.webview)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITTED:
            # Evaluate a script to get the DOM
            script = "document.documentElement.outerHTML"
            self.webview.evaluate_script(script, self.on_script_evaluated)

    def on_script_evaluated(self, webview, result):
        # This is where you can process the result
        if result.get_type() == WebKit2.JavascriptResultType.VALUE:
            html_content = result.get_js_value().to_string()
            print("DOM Loaded:")
            print(html_content)

if __name__ == "__main__":
    WebViewExample()
    Gtk.main()
