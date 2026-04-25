
import sys
from gi.repository import Gtk, WebKit

class WebViewExample:

    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        self.webview.connect("load-finished", self.on_load_finished)
        self.webview.load_uri("http://www.example.com")

        self.window.add(self.webview)
        self.window.set_size_request(800, 600)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def on_load_finished(self, webview, frame):
        script = "document.documentElement.outerHTML;"
        frame.evaluate_script(script)

    def evaluate_script(self, result):
        print("DOM content:", result)

if __name__ == "__main__":
    WebViewExample()
    Gtk.main()
