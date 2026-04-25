
import gtk
import webkit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    frame.execute_script("document.documentElement.outerHTML", get_dom)

def get_dom(result):
    print("DOM loaded:")
    print(result)

def main():
    # Create a GTK window and a WebView
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished event
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Set up the window
    window.add(webview)
    window.set_default_size(800, 600)
    window.connect("destroy", gtk.main_quit)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
