
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the innerHTML of the body
    frame.evaluate('document.body.innerHTML', None, on_dom_received)

def on_dom_received(result, frame):
    print("DOM Content:")
    print(result)

def main():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a URL
    webview.load_uri("http://www.example.com")

    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
