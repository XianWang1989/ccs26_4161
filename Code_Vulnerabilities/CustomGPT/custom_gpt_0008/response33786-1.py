
import gtk
import webkit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    dom_content = webview.evaluate_javascript("document.documentElement.outerHTML")
    print(dom_content)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load-finished", load_finished)

    # Load a URL
    webview.load_uri("http://example.com")

    # Add the WebView to the window and show everything
    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
