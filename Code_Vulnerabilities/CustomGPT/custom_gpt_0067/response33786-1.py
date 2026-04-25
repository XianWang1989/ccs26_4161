
import webkit
import gtk

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    webview.run_javascript("document.documentElement.outerHTML", callback)

def callback(result):
    if result:
        print("DOM Loaded:")
        print(result)  # This will print the HTML source

if __name__ == "__main__":
    # Initialize GTK and create a WebView
    gtk.main()
    webview = webkit.WebView()

    # Connect the load-finished signal
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("https://example.com")

    # Show the WebView
    webview.show()
    gtk.main()
