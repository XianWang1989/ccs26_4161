
import gtk
import webkit

def on_load_finished(webview, frame):
    # Use JavaScript to get the DOM
    frame.evaluate("document.documentElement.outerHTML", on_html_received)

def on_html_received(result):
    print("HTML Content:")
    print(result)

# Set up the main GTK window
window = gtk.Window()
window.set_title("WebKit DOM Example")
window.set_size_request(800, 600)
webview = webkit.WebView()

# Connect the load finished event
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.open("https://www.example.com")

window.add(webview)
window.show_all()

# Start the GTK main loop
gtk.main()
