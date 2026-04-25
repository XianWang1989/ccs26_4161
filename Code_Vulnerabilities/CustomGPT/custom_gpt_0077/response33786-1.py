
import gtk
import webkit

class MyWebKitApp:
    def __init__(self):
        self.window = gtk.Window()
        self.webview = webkit.WebView()
        self.webview.connect("load-finished", self.on_load_finished)

        self.window.add(self.webview)
        self.window.set_default_size(800, 600)
        self.window.connect("destroy", gtk.main_quit)
        self.window.show_all()

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        script = "document.documentElement.outerHTML"
        frame.evaluate_script(script, self.on_script_executed)

    def on_script_executed(self, result, error):
        if error:
            print("Error executing script:", error)
        else:
            print("DOM content:", result)

    def load_page(self, url):
        self.webview.load_uri(url)

if __name__ == "__main__":
    app = MyWebKitApp()
    app.load_page("http://example.com")
    gtk.main()
