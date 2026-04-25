
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    frame.evaluate('document.documentElement.outerHTML', callback)

def callback(result):
    # This function will be called with the result of the JavaScript execution
    print("DOM content:")
    print(result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished signal
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.open("http://example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
