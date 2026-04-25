
import gi
gi.require_version('WebKit', '4.0')
from gi.repository import Gtk, WebKit

class WebKitExample:
    def __init__(self):
        self.window = Gtk.Window()
        self.webview = WebKit.WebView()

        # Connect the loadFinished signal
        self.webview.connect('load-finished', self.on_load_finished)

        # Load a sample URL
        self.webview.load_uri('https://www.example.com')
        self.window.add(self.webview)
        self.window.set_default_size(800, 600)
        self.window.connect('destroy', Gtk.main_quit)
        self.window.show_all()

    def on_load_finished(self, webview, frame):
        # Execute a script to get the DOM content
        script = 'document.documentElement.outerHTML'
        webview.evaluate_script(script, self.script_evaluated)

    def script_evaluated(self, webview, result, user_data):
        if result:
            print("DOM Content:")
            print(result)

if __name__ == "__main__":
    app = WebKitExample()
    Gtk.main()
