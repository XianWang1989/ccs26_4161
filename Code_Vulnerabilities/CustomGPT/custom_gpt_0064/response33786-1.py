
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to retrieve the DOM as a string
    frame.evaluate_script("document.documentElement.outerHTML", callback)

def callback(result, *data):
    # This function is called when the JavaScript execution is complete
    print("DOM content:")
    print(result)  # Output the DOM content

def main():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    window.add(webview)
    window.set_size_request(800, 600)
    window.show_all()

    webview.load_uri("http://example.com")  # Replace with your target URL

    gtk.main()

if __name__ == "__main__":
    main()
