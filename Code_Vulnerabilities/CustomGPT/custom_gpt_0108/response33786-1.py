
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript function to get the DOM
    webview.evaluate_javascript("document.documentElement.outerHTML", on_js_result)

def on_js_result(result):
    # This function is called with the result of the JavaScript execution
    print("DOM Content:\n", result)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.connect("delete-event", gtk.main_quit)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a web page
    webview.load_uri("http://example.com")

    # Add the WebView to the window
    window.add(webview)
    window.set_default_size(800, 600)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
