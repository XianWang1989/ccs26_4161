
import gtk
import webkit

class MyWebView:
    def __init__(self):
        # Create the GTK window
        self.window = gtk.Window()
        self.window.connect("destroy", gtk.main_quit)

        # Create a WebView and add it to the window
        self.webview = webkit.WebView()
        self.webview.connect("load-finished", self.on_load_finished)
        self.window.add(self.webview)

        # Load a web page
        self.webview.load_uri("http://www.example.com")

        # Show the window
        self.window.set_size_request(800, 600)
        self.window.show_all()

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        js_code = "document.documentElement.outerHTML"
        webview.evaluate_script(js_code, self.on_js_result)

    def on_js_result(self, result):
        # This method gets called with the result of the JavaScript execution
        if result is not None:
            print("DOM Content: ", result)
        else:
            print("Failed to retrieve the DOM.")

if __name__ == "__main__":
    # Initialize GTK
    gtk.main()

    # Create and run the MyWebView class instance
    app = MyWebView()
    gtk.main()
