
import gtk
import webkit

def load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    frame.execute_script("document.documentElement.outerHTML", callback=handle_dom)

def handle_dom(result):
    print("DOM content:")
    print(result)  # This will contain the full HTML of the page

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished signal
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
