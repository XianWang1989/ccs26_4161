
import gtk
import webkit

def on_load_finished(webview, frame):
    # This JavaScript code gets the entire HTML document
    js_code = "document.documentElement.outerHTML"

    # Evaluate the script in the context of the loaded page
    frame.evaluate_script(js_code, callback=lambda result: print(result))

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect to the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.set_default_size(800, 600)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
