
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2


def on_load_finished(webview, frame):
    # Ensure the frame is the main frame
    if frame == webview.get_main_frame():
        # Execute JavaScript to get the HTML content of the document
        script = "document.documentElement.outerHTML"
        webview.run_javascript(script, None, None, None)


def on_javascript_result(webkit_js_result, webview):
    # Get the result of the JavaScript execution
    webkit_js_result.get_js_value()  # This method can be used to retrieve the value


# Create a GTK window
window = Gtk.Window(title="WebKit2 DOM Example")
webview = WebKit2.WebView()

# Connect the load-finished signal
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.load_uri("https://www.example.com")
window.add(webview)

# Show the GTK window
window.connect("destroy", Gtk.main_quit)
window.set_default_size(800, 600)
window.show_all()

# Start the GTK main loop
Gtk.main()
