
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class WebViewer(Gtk.Window):
    def __init__(self):
        super(WebViewer, self).__init__()
        self.set_default_size(800, 600)

        self.webview = WebKit2.WebView()
        self.webview.connect("load-changed", self.on_load_changed)

        self.add(self.webview)
        self.webview.load_uri("https://www.example.com")
        self.show_all()

    def on_load_changed(self, webview, load_event):
        if load_event == WebKit2.LoadEvent.COMMITTED:
            self.get_dom()

    def get_dom(self):
        # Execute JavaScript to get the DOM
        self.webview.evaluate_javascript("document.documentElement.outerHTML",
                                          self.on_dom_retrieved)

    def on_dom_retrieved(self, result, error):
        if error is None:
            print("DOM Retrieved:")
            print(result)  # result contains the HTML content
        else:
            print("Error retrieving DOM:", error)

if __name__ == '__main__':
    app = WebViewer()
    Gtk.main()
