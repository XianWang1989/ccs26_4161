
import gtk
import webkit

def on_load_finished(webview, frame):
    # This function is called when the page has finished loading
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML;"

    # Evaluate the script
    frame.evaluate(script, callback)

def callback(result):
    # This function will handle the result of the JavaScript evaluation
    print("DOM Content:")
    print(result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect to the load-finished signal
    webview.connect("load-finished", on_load_finished)

    webview.load_uri("http://example.com")  # Load your desired URL

    window.add(webview)
    window.connect("destroy", gtk.main_quit)
    window.set_size_request(800, 600)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
