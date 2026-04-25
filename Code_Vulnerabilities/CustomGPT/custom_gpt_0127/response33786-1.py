
import gtk
import webkit

def load_finished(webview, frame):
    # This function is called when the page finishes loading
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    frame.execute_script(script)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_size_request(800, 600)

    # Create a WebKit WebView
    webview = webkit.WebView()
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the WebView to the window and show everything
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
