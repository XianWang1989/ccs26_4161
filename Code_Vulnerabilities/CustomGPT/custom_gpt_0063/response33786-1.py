
import gtk
import webkit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    js_code = "document.documentElement.outerHTML"
    webview.evaluate_script(js_code, handle_result)

def handle_result(result):
    print("DOM content loaded:")
    print(result)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_title("WebKit Example")
    window.set_size_request(800, 600)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load_finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the WebView to the window
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
