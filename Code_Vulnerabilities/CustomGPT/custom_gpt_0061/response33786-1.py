
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    frame.evaluate_script("document.documentElement.outerHTML", on_dom_ready)

def on_dom_ready(result):
    print("DOM Content:")
    print(result)

# Initialize GTK and WebKit
window = gtk.Window()
webview = webkit.WebView()

# Connect the load-finished event to the callback
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.load_uri("http://example.com")

# Set up the window
window.add(webview)
window.show_all()
gtk.main()
