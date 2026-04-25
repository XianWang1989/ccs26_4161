
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    frame.execute_script(script)

def on_script_finished(webview, frame, result):
    print("DOM Content:", result)

# Create a WebView
webview = webkit.WebView()
webview.connect('load_finished', on_load_finished)
webview.connect('script_finished', on_script_finished)

# Load a webpage
webview.load_uri("http://example.com")

# Show the window
window = gtk.Window()
window.add(webview)
window.show_all()
gtk.main()
