
import gtk
import webkit

def load_finished_callback(webview, frame):
    # Execute JavaScript to get the DOM content
    script = "document.documentElement.outerHTML"
    webview.execute_script(script, on_script_executed)

def on_script_executed(result, exception):
    if exception is not None:
        print("Error executing script: ", exception)
    else:
        print("DOM content: ", result)

def main():
    # Create the GTK window
    window = gtk.Window()
    window.set_title("WebKit Example")
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load-finished", load_finished_callback)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the WebView to the window and show everything
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
