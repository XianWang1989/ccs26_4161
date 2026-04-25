
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk

class WebViewApp:
    def __init__(self):
        self.window = Gtk.Window(title="WebKit DOM Example")
        self.webview = WebKit2.WebView()

        self.webview.connect("load-changed", self.on_load_changed)

        self.window.add(self.webview)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_default_size(800, 600)
        self.window.show_all()

        self.webview.load_uri("https://www.example.com")

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.FINISHED:
            # Execute JavaScript to get the DOM
            self.webview.evaluate_script("document.documentElement.outerHTML;").connect("response", self.on_script_response)

    def on_script_response(self, webview, result):
        # Get the result of the JavaScript execution
        data = result.get_data()
        print("DOM Content:", data)

if __name__ == "__main__":
    app = WebViewApp()
    Gtk.main()
