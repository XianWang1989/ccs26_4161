
import gi
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2

class MyWebView:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit2.WebView()

        self.webview.connect("load-changed", self.on_load_changed)
        self.window.add(self.webview)
        self.window.show_all()

        self.webview.load_uri("http://example.com")  # Load your desired URI

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITTED:
            # Once the page is committed, we can evaluate a script to get the DOM
            self.webview.evaluate_script("document.documentElement.outerHTML", self.on_script_evaluated)

    def on_script_evaluated(self, webview, result, error):
        if error is not None:
            print("Error evaluating script:", error)
            return

        # Print the DOM
        print("DOM:", result.get_string())

if __name__ == "__main__":
    MyWebView()
    Gtk.main()
