
import gi
gi.require_version('WebKit', '3.0')
from gi.repository import WebKit, Gtk

class MyWebView(Gtk.Window):
    def __init__(self):
        super(MyWebView, self).__init__()
        self.set_default_size(800, 600)

        self.webview = WebKit.WebView()
        self.webview.connect('load-finished', self.on_load_finished)
        self.webview.load_uri("http://example.com")

        self.add(self.webview)
        self.show_all()

    def on_load_finished(self, webview, frame):
        dom_document = frame.get_dom_document()
        # Now you can manipulate the DOM document as needed
        print(dom_document)

if __name__ == "__main__":
    window = MyWebView()
    Gtk.main()
