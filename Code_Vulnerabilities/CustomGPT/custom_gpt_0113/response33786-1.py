
import gtk
import webkit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    webview.evaluate_script(script, callback)

def callback(result, error):
    if error:
        print("Error:", error)
    else:
        print("DOM:", result)

# Create the GTK window and WebView
window = gtk.Window()
webview = webkit.WebView()

# Connect to the load-finished event
webview.connect("load-finished", load_finished)

# Load the desired webpage
webview.load_uri("http://example.com")

# Add WebView to the window and show everything
window.add(webview)
window.show_all()

# Start the GTK main loop
gtk.main()
