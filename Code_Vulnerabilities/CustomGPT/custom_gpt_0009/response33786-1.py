
import gtk
import webkit

def on_load_finished(webview, frame):
    # JavaScript code to get the DOM
    js_code = "document.documentElement.outerHTML;"

    # Evaluate the JavaScript and get the result
    webview.evaluate_javascript(js_code, callback)

def callback(result, error):
    if error is not None:
        print("Error evaluating JavaScript: ", error)
    else:
        print("DOM Content: ", result)

# Create a WebKit WebView
window = gtk.Window()
webview = webkit.WebView()

# Connect to the load finished event
webview.connect("load-finished", on_load_finished)

# Load a URL
webview.load_uri("http://example.com")

# Show the window
window.add(webview)
window.show_all()
gtk.main()
