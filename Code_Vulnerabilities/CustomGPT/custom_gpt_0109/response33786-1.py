
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    frame.evaluate_script(script, callback=on_script_evaluated)

def on_script_evaluated(result):
    if result is not None:
        print("DOM Content Retrieved:")
        print(result)

# Set up the WebView
window = gtk.Window()
webview = webkit.WebView()

# Connect the load-finished event to the handler
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.open("http://example.com")

# Add the webview to the window and show everything
window.add(webview)
window.show_all()

gtk.main()
