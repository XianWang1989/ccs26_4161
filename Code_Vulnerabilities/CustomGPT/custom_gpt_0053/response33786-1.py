
import gtk
import webkit

def load_finished(web_view, frame):
    # JavaScript to retrieve the DOM as a string
    js_code = "document.documentElement.outerHTML"

    # Evaluate the JavaScript code in the context of the frame
    frame.execute_script(js_code, frame)

def script_finished(web_view, frame, result):
    # This function executes when the JavaScript is finished
    print("DOM Content:")
    print(result)

# Set up the GTK window and WebView
window = gtk.Window()
web_view = webkit.WebView()

# Connect to the load-finished event
web_view.connect("load-finished", load_finished)
web_view.connect("script-finished", script_finished)

# Load a webpage
web_view.open("https://example.com")

# Add the WebView to the window and show everything
window.add(web_view)
window.set_size_request(800, 600)
window.connect("destroy", gtk.main_quit)
window.show_all()

gtk.main()
