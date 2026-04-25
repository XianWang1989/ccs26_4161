
import gtk
from webkit import WebKit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    frame.evaluate_script("document.documentElement.outerHTML")

def main():
    # Initialize GTK
    gtk.main()

    # Create a new WebView
    webview = WebKit.WebView()
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Display the WebView
    window = gtk.Window()
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
