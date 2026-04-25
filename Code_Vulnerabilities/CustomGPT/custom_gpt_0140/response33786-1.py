
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    js_code = "document.documentElement.outerHTML"
    frame.evaluate_javascript(js_code, on_js_evaluated)

def on_js_evaluated(result, frame):
    print("DOM HTML:")
    print(result)

# Set up the WebView
def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load finished event
    webview.connect("load-finished", on_load_finished)

    # Load a web page
    webview.load_uri("https://www.example.com")

    # Add the WebView to the window and show everything
    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
