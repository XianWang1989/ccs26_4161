
import sys
from gi.repository import WebKit, Gtk

class Browser:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        self.webview.connect("load-finished", self.on_load_finished)
        self.webview.load_uri("https://example.com")

        self.window.add(self.webview)
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        script = "document.documentElement.outerHTML"
        webview.evaluate(script, self.on_dom_received, None)

    def on_dom_received(self, result, user_data):
        if isinstance(result, WebKit.ScriptResult):
            html_content = result.get_string()
            print(html_content)  # Output the HTML content

if __name__ == "__main__":
    Gtk.init(sys.argv)
    browser = Browser()
    Gtk.main()
