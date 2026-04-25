
import gtk
import webkit

def on_load_finished(webview, frame):
    # This function will be called when the page finishes loading
    js_code = "document.documentElement.outerHTML"
    frame.evaluate_script(js_code)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load finished event
    webview.connect("load_finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
