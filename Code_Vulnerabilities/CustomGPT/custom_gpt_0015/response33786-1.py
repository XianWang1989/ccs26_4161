
import gtk
import webkit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    frame.evaluate(script, callback)

def callback(result, frame):
    # This callback function is invoked with the result of the script
    if result is not None:
        print("DOM content:")
        print(result)
    else:
        print("Failed to retrieve DOM content.")

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished signal
    webview.connect("load_finished", load_finished)

    # Load a web page
    webview.load_uri("http://example.com")

    window.add(webview)
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
