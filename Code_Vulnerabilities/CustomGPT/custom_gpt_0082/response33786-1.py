
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.innerHTML"
    webview.evaluate_script(script, callback)

def callback(result):
    if result:
        print("DOM Content:")
        print(result)

def main():
    # Initialize GTK
    window = gtk.Window()
    window.set_size_request(800, 600)
    window.connect("delete-event", gtk.main_quit)

    # Create WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a URL
    webview.load_uri("http://example.com")
    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
