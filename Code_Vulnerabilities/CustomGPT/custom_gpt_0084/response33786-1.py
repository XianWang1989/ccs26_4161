
import gtk
import webkit

def on_load_finished(webview, frame, request):
    # Evaluate JavaScript to get the DOM
    dom = frame.evaluate_script("document.documentElement.outerHTML")
    print(dom)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_size_request(800, 600)

    # Create WebKit WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("https://www.example.com")

    # Add the webview to the window and show everything
    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
