
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to retrieve the DOM content
    script = "document.documentElement.outerHTML"
    frame.run_javascript(script, None, None, None)

def on_javascript_finished(webview, frame, result, data):
    print("DOM Content:")
    print(result)  # This will print the HTML content of the page

# Set up the GTK window and WebView
window = gtk.Window()
window.set_default_size(800, 600)

webview = webkit.WebView()
webview.connect('load-finished', on_load_finished)

# Setup callback to get the result of the JavaScript execution
webview.connect('run-javascript', on_javascript_finished)

# Load a web page
webview.load_uri("http://www.example.com")

# Add WebView to the window and show everything
window.add(webview)
window.show_all()

# Start the GTK main loop
gtk.main()
