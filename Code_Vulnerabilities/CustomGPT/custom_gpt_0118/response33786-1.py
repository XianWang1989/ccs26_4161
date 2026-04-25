
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    js_code = "document.documentElement.outerHTML;"
    frame.evaluate_javascript(js_code, callback)

def callback(result):
    print("DOM Content:")
    print(result)

# Create a WebKit web view
webview = webkit.WebView()
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.open("http://example.com")

# Start the GTK main loop
gtk.main()
