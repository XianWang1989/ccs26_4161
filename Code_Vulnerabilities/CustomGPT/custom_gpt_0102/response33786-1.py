
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the entire DOM
    frame.evaluate("document.documentElement.outerHTML", on_dom_retrieved)

def on_dom_retrieved(result, frame):
    print("DOM Retrieved:")
    print(result)

# Setup WebView
window = gtk.Window()
webview = webkit.WebView()

# Connect to the load-finished signal
webview.connect("load-finished", on_load_finished)
webview.load_uri("http://example.com")  # Replace with your desired URL

# Add the webview to the window and show it
window.add(webview)
window.show_all()
gtk.main()
