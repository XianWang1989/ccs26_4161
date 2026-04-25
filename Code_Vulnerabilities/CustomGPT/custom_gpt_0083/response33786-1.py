
import gtk
import webkit

def load_finished(webview, frame):
    # Check if the frame is the main frame
    if frame == webview.get_main_frame():
        # Execute JavaScript to get the DOM
        webview.evaluate_script("document.documentElement.outerHTML;", dom_loaded)

def dom_loaded(result):
    print("DOM Loaded:")
    print(result)

def main():
    # Set up the GTK window and WebView
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load finished event
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add WebView to the window and show everything
    window.add(webview)
    window.set_size_request(800, 600)
    window.show_all()
    window.connect("destroy", gtk.main_quit)

    gtk.main()

if __name__ == "__main__":
    main()
