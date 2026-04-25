
import gtk
import webkit

def webview_load_finished(webview, frame):
    # This callback is called when the web view has finished loading.
    # Execute JavaScript to get the DOM content
    webview.execute_script("document.documentElement.outerHTML;", handle_dom_result)

def handle_dom_result(result):
    # This function will handle the result of the JavaScript execution
    print("DOM Content:")
    print(result)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_title("WebKit Example")
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)

    # Create a WebView and connect to its load-finished signal
    webview = webkit.WebView()
    webview.connect("load-finished", webview_load_finished)

    # Load a desired URL
    webview.load_uri("http://www.example.com")

    # Add the WebView to the window and show everything
    window.add(webview)
    webview.show()
    window.show()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
