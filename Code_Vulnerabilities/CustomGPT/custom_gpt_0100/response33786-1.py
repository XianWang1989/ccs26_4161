
import gtk
import webkit

class WebViewExample:

    def __init__(self):
        self.window = gtk.Window()
        self.webview = webkit.WebView()

        # Connect to the load-finished signal
        self.webview.connect("load-finished", self.on_load_finished)

        # Load a URL
        self.webview.load_uri("http://example.com")
        self.window.add(self.webview)
        self.window.show_all()

    def on_load_finished(self, webview, frame):
        # Evaluate JavaScript to get the DOM
        script = "document.documentElement.innerHTML"
        webview.evaluate_script(script, self.dom_callback)

    def dom_callback(self, result, user_data):
        print("DOM Content:", result)  # Print the DOM

if __name__ == "__main__":
    gtk.main()
