
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2, Gtk

class Browser(Gtk.Window):
    def __init__(self):
        super(Browser, self).__init__()

        self.set_title("WebKit DOM Example")
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)
        self.webview.load_uri("https://www.example.com")

        self.add(self.webview)
        self.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITTED:
            self.get_dom_document()

    def get_dom_document(self):
        javascript_code = "document.documentElement.outerHTML"
        self.webview.run_javascript(javascript_code, None, self.on_javascript_finished, None)

    def on_javascript_finished(self, result, error):
        if error:
            print("JavaScript execution error:", error.message)
            return

        html_content = result.get_js_value()  # Extract HTML content
        print("DOM Content:", html_content)

if __name__ == "__main__":
    Gtk.init()
    browser = Browser()
    Gtk.main()
