
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the document's HTML
    frame.evaluate_script("document.documentElement.outerHTML", 
                           callback=on_get_html)

def on_get_html(html):
    # This callback receives the HTML content
    print("Page HTML:")
    print(html)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect to the load-finished event
    webview.connect("load-finished", on_load_finished)

    window.add(webview)
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)

    # Load a webpage
    webview.load_uri("http://example.com")
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
