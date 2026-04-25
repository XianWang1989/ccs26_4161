
import gtk
import webkit

def on_load_finished(web_view, frame):
    # Evaluate JavaScript to get the DOM content
    js_code = "document.documentElement.outerHTML;"
    frame.evaluate_script(js_code)

def on_script_finished(web_view, frame, result):
    # This callback receives the result of the executed script
    print("DOM Content:")
    print(result)

# Set up the WebView and connect signals
window = gtk.Window()
web_view = webkit.WebView()

# Connect the load-finished signal
web_view.connect("load-finished", on_load_finished)
web_view.connect("evaluate-script-finished", on_script_finished)

# Load a URL
web_view.load_uri("http://example.com")

# Packing the WebView in a window
window.add(web_view)
window.show_all()

gtk.main()
