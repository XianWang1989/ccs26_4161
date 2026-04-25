
import gtk
import webkit

def on_load_finished(webview, frame):
    # Evaluate JavaScript to get the DOM content
    dom_content = webview.evaluate_script("document.documentElement.outerHTML")
    print(dom_content)

# Create the WebView
window = gtk.Window()
webview = webkit.WebView()

# Connect the load-finished event
webview.connect("load-finished", on_load_finished)

# Load a page
webview.load_uri("http://example.com")
window.add(webview)
window.show_all()

# Start the GTK main loop
gtk.main()
