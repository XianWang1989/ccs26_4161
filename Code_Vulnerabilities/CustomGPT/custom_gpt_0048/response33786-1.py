
import sys
from gi.repository import WebKit, Gtk

class MyWebView:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        self.webview.connect("load-finished", self.on_load_finished)
        self.window.add(self.webview)
        self.window.show_all()

        self.webview.open("http://example.com")

        self.window.connect("destroy", Gtk.main_quit)

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        webview.run_javascript("document.documentElement.outerHTML", self.dom_callback)

    def dom_callback(self, result, frame):
        if result:
            print(result.get_data())  # The DOM is in HTML format
        else:
            print("Failed to retrieve the DOM")

if __name__ == '__main__':
    Gtk.init(sys.argv)
    MyWebView()
    Gtk.main()
