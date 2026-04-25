
import gtk
import webkit

def on_load_finished(web_view, frame):
    # JavaScript to get the entire DOM
    js_code = "document.documentElement.outerHTML"
    frame.evaluate_script(js_code)

def receive_dom_value(web_view, frame, result, user_data):
    if result:
        print("DOM content retrieved:")
        print(result)

# Create a WebKit WebView
web_view = webkit.WebView()

# Connect to the load-finished signal
web_view.connect("load-finished", on_load_finished)

# Connect the signal to receive the DOM value
frame = web_view.get_main_frame()
frame.connect("evaluate-javascript", receive_dom_value)

# Load a webpage
web_view.load_uri("http://example.com")

# Start the GTK main loop
gtk.main()
