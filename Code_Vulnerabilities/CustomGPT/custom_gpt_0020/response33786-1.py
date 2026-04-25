
import gtk
import webkit

def load_finished(webview, frame):
    # This function is called when the page has finished loading.
    # Execute JavaScript to get the DOM.
    webview.execute_script("var dom = document.documentElement.outerHTML; dom;")

def on_script_finished(webview, script_result):
    # This function is called after the script is executed.
    print("DOM Content:")
    print(script_result)

# Setup the main GTK window
window = gtk.Window()
window.set_default_size(800, 600)
window.connect("destroy", gtk.main_quit)

# Create a WebView
webview = webkit.WebView()
webview.connect("load-finished", load_finished)

# Connect the 'run-javascript-finished' signal to get result from script execution
webview.connect("script-finished", on_script_finished)

# Load a webpage
webview.load_uri("http://example.com")
window.add(webview)

# Show all widgets
window.show_all()

# Start the GTK main loop
gtk.main()
