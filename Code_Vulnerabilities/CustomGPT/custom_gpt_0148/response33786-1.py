
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    js_code = "document.documentElement.outerHTML"
    frame.evaluate_javascript(js_code, callback)

def callback(result):
    print("DOM Content Loaded:")
    print(result)

def main():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    webview.load_uri("http://example.com")  # Replace with your URL
    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
