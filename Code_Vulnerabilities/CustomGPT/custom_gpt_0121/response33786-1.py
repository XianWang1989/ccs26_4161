
from gi.repository import WebKit2, Gtk

class MyWebView:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit2.WebView()

        # Connect the load finished signal
        self.webview.connect("load-finished", self.on_load_finished)

        self.window.add(self.webview)
        self.window.show_all()
        self.webview.load_uri("https://example.com")  # Load your desired URL

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        script = "document.documentElement.outerHTML"
        webview.evaluate_javascript(script, self.java_script_callback)

    def java_script_callback(self, webview, result, user_data):
        if result.get_type() == WebKit2.JavascriptResultType.VALUE:
            html_content = result.get_js_value().to_string()
            print(html_content)  # This contains the HTML of the loaded page
        else:
            print("Error executing JavaScript")

if __name__ == "__main__":
    Gtk.init()
    app = MyWebView()
    Gtk.main()
