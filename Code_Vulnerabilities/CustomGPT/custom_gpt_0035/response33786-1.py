
from gi.repository import WebKit, Gtk

def load_finished(web_view, frame):
    # Ensure the frame is fully loaded before accessing the DOM
    if frame.get_status() == WebKit.LoadStatus.FINISHED:
        # Execute JavaScript to get the DOM content
        frame.evaluate_script("document.documentElement.outerHTML")

# Set up the WebView
web_view = WebKit.WebView()
web_view.connect("load_finished", load_finished)

# Load a web page
web_view.load_uri('https://www.example.com')

# Main GTK loop
window = Gtk.Window()
window.add(web_view)
window.show_all()
Gtk.main()
