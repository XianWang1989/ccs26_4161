
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    frame.execute_script(script, callback)

def callback(result):
    print("DOM content:")
    print(result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load_finished signal
    webview.connect("load-finished", on_load_finished)

    # Load a URL
    webview.load_uri("http://example.com")

    # Add WebView to the window
    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
