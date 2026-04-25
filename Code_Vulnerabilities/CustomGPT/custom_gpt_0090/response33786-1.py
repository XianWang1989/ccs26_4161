
import gtk
import webkit

class MyWebView:
    def __init__(self):
        self.window = gtk.Window()
        self.webview = webkit.WebView()
        self.webview.connect("load-finished", self.on_load_finished)
        self.window.add(self.webview)
        self.window.show_all()
        self.webview.load_uri("http://example.com")

    def on_load_finished(self, webview, frame):
        # Execute JavaScript to get the DOM
        webview.evaluate_script("document.documentElement.outerHTML", self.on_dom_retrieved)

    def on_dom_retrieved(self, result, error):
        if error:
            print("Error retrieving DOM:", error)
        else:
            print("DOM content:", result)

if __name__ == "__main__":
    gtk.main()
