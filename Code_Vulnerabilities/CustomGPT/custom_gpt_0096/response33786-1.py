
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    webview.evaluate_javascript("document.documentElement.outerHTML;", handle_dom_result)

def handle_dom_result(result):
    # This function will handle the result of the JavaScript execution
    print("DOM Loaded:")
    print(result)  # Here you will see the HTML content of the page

def main():
    # Set up the GTK window
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a URL
    webview.load_uri("http://example.com")

    # Add the WebView to the window
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
