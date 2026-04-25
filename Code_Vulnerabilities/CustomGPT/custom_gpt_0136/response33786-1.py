
import gtk
import webkit

class WebViewExample:

    def __init__(self):
        self.window = gtk.Window()
        self.webview = webkit.WebView()

        self.webview.connect("load-finished", self.on_load_finished)
        self.webview.load_uri("http://example.com")  # Replace with your URL

        self.window.add(self.webview)
        self.window.set_size_request(800, 600)
        self.window.connect("destroy", gtk.main_quit)
        self.window.show_all()

    def on_load_finished(self, webview, frame):
        # JavaScript to fetch the entire DOM
        js_script = "document.documentElement.outerHTML"
        webview.evaluate(js_script, self.on_dom_retrieved)

    def on_dom_retrieved(self, result):
        if isinstance(result, str):
            print("DOM Retrieved:\n", result)
        else:
            print("Failed to retrieve DOM")

if __name__ == "__main__":
    gtk.main()
