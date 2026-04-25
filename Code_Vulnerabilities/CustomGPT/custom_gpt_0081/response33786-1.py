
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    javascript = "document.documentElement.outerHTML;"
    frame.evaluate_javascript(javascript, callback_function)

def callback_function(result, error):
    if error is not None:
        print(f"Error: {error}")
    else:
        print("DOM Content:")
        print(result)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_title("WebKit DOM Example")
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the WebView to the window
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
