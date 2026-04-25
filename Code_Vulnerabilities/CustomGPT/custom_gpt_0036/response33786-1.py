
import gtk
import webkit

class WebViewApp:
    def __init__(self):
        self.window = gtk.Window()
        self.window.connect("destroy", gtk.main_quit)

        self.webview = webkit.WebView()
        self.webview.connect("load-finished", self.on_load_finished)

        self.window.add(self.webview)
        self.window.set_default_size(800, 600)
        self.window.show_all()

        # Load a webpage
        self.webview.load_uri("http://example.com")

    def on_load_finished(self, webview, frame):
        # After the page has loaded, evaluate JavaScript to get the DOM
        script = "document.documentElement.outerHTML;"
        webview.evaluate_script(script, self.on_script_evaluated)

    def on_script_evaluated(self, result, exception):
        if exception:
            print("Error evaluating script:", exception)
        else:
            print("DOM content retrieved:")
            print(result)  # This will print the entire DOM as a string

if __name__ == "__main__":
    app = WebViewApp()
    gtk.main()
