
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    webview.execute_script("document.documentElement.outerHTML", on_get_dom)

def on_get_dom(result):
    print("DOM content:")
    print(result)

def main():
    # Set up the WebKit WebView
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished signal to the callback
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the WebView to the window and show it
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
