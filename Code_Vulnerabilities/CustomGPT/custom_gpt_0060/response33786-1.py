
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk

class WebViewExample:
    def __init__(self):
        # Create a GTK Window
        self.window = Gtk.Window()
        self.window.set_title("WebKit DOM Example")
        self.window.set_default_size(800, 600)

        # Create a WebKit WebView
        self.webview = WebKit2.WebView()
        self.webview.load_uri("https://www.example.com")

        # Connect the load finished signal
        self.webview.connect('load-finished', self.on_load_finished)

        # Add the WebView to the Window
        self.window.add(self.webview)
        self.window.show_all()

        # Connect window close event
        self.window.connect("destroy", Gtk.main_quit)

    def on_load_finished(self, webview, navigation_action):
        # Execute JavaScript to get the DOM content after the page has loaded
        self.webview.run_javascript("document.documentElement.outerHTML;", None, self.on_dom_ready, None)

    def on_dom_ready(self, webview, result, error):
        if error is None:
            # Here you can access the DOM
            dom_string = result.get_js_value().to_string()
            print("DOM content:", dom_string)
        else:
            print("Error retrieving DOM:", error)

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = WebViewExample()
    app.run()
