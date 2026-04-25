
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    frame.execute_script("document.documentElement.outerHTML")

def on_load_committed(webview, frame):
    # Connect load finished signal
    webview.connect("load-finished", on_load_finished)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect signals
    webview.connect("load-committed", on_load_committed)

    # Load a website
    webview.load_uri("http://example.com")

    window.add(webview)
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
