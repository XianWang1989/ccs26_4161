
import gi
gi.require_version('WebKit', '3.0')
from gi.repository import WebKit, Gtk

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    script = "document.documentElement.outerHTML;"
    frame.evaluate_javascript(script, None, None, None)

    # Add a callback to handle the result
    frame.evaluate_javascript(script, handle_dom_result, None, None)

def handle_dom_result(result, *args):
    # This function will be called with the DOM content
    print("DOM content:")
    print(result)

# Create a Gtk.Window and a WebView
window = Gtk.Window()
webview = WebKit.WebView()

# Connect the load_finished signal to the handler
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.load_uri("http://example.com")

# Set up the window
window.add(webview)
window.set_default_size(800, 600)
window.connect("destroy", Gtk.main_quit)
window.show_all()

# Start the GTK main loop
Gtk.main()
