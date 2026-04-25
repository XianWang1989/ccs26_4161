
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class MyWebView(Gtk.Window):
    def __init__(self):
        super().__init__(title="WebKit DOM Example")

        self.webview = WebKit2.WebView()
        self.webview.connect("load-finished", self.on_load_finished)

        self.webview.load_uri("https://example.com")
        self.add(self.webview)

    def on_load_finished(self, webview, navigation_action):
        # Evaluate JavaScript to get the DOM
        js = "document.documentElement.outerHTML"
        self.webview.evaluate_script(js, self.on_script_evaluated)

    def on_script_evaluated(self, webview, result, error):
        if error:
            print("Error evaluating script:", error.message)
        else:
            print("DOM HTML:", result)

win = MyWebView()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
