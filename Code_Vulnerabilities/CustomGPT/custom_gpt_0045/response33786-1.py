
import gi
gi.require_version('WebKit', '4.0')
from gi.repository import WebKit, Gtk

class MyWebView(Gtk.Window):
    def __init__(self):
        super(MyWebView, self).__init__()

        self.webview = WebKit.WebView()
        self.webview.connect("load-finished", self.on_load_finished)
        self.webview.load_uri("http://example.com")

        self.add(self.webview)
        self.set_size_request(800, 600)
        self.set_title("WebKit DOM Example")
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_load_finished(self, webview, frame):
        # Executing JavaScript to get the inner HTML of the body
        frame.execute_script("document.body.innerHTML", self.js_callback)

    def js_callback(self, result):
        if result.get_value_type() == WebKit.WebKitWebView.ScriptResultType.STRING:
            # This gets the inner HTML of the body
            html_content = result.get_string()
            print("DOM after the page has loaded:")
            print(html_content)
        else:
            print("Failed to get the DOM content.")

if __name__ == "__main__":
    Gtk.init([])
    MyWebView()
    Gtk.main()
