
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the HTML content of the DOM
    webview.execute_script("document.documentElement.outerHTML", on_dom_retrieved)

def on_dom_retrieved(result):
    print("DOM Content:")
    print(result)  # The DOM content is printed here

def main():
    # Create a GTK window and WebView
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Set up the window
    window.add(webview)
    window.connect("destroy", gtk.main_quit)
    window.set_size_request(800, 600)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
