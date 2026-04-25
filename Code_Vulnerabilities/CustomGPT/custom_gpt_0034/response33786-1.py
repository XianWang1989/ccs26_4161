
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk

class WebViewExample(Gtk.Window):
    def __init__(self):
        super().__init__(title="WebKit DOM Example")
        self.set_default_size(800, 600)

        # Create a WebView
        self.webview = WebKit2.WebView()
        self.webview.load_finished.connect(self.on_load_finished)

        # Load a webpage
        self.webview.load_uri("https://www.example.com")

        # Add the WebView to the window
        self.add(self.webview)

    def on_load_finished(self, webview, loading_event):
        if loading_event:
            # Execute JavaScript to get the DOM
            self.webview.run_javascript("document.documentElement.outerHTML", None, self.on_dom_retrieved, None)

    def on_dom_retrieved(self, result, error):
        if error is None:
            # Output the DOM
            print(result.get_data().decode('utf-8'))
        else:
            print("Error retrieving DOM:", error)

if __name__ == "__main__":
    app = WebViewExample()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
