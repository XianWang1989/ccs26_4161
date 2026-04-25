
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    webview.evaluate_script("document.documentElement.outerHTML", callback)

def callback(result):
    if result is not None:
        print("DOM loaded:")
        print(result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
