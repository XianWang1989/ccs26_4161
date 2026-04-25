
import gtk
import webkit

def on_load_finished(webview, frame):
    # JavaScript to get the DOM as a string
    js_code = "document.documentElement.outerHTML;"

    # Evaluate the JavaScript
    frame.evaluate_script(js_code, callback)

def callback(result):
    if result is not None:
        print("DOM Content:")
        print(result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    webview.connect("load-finished", on_load_finished)

    # Load a URL
    webview.load_uri('http://example.com')

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
