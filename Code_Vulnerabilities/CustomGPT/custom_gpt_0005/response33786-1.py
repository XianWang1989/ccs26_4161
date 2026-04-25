
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    frame.evaluate_script("document.documentElement.outerHTML")

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load finished signal
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Set up the window
    window.add(webview)
    window.connect("destroy", gtk.main_quit)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
