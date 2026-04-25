
import gtk
import webkit

def load_finished(view, frame):
    # This function is called when the page has finished loading
    script = "document.documentElement.innerHTML"
    # Evaluate the JavaScript to get the DOM
    view.evaluate_javascript(script, load_callback)

def load_callback(result):
    # This callback is called with the result of the JavaScript evaluation
    print("DOM Content:")
    print(result)

def main():
    # Create the GTK window and WebView
    window = gtk.Window()
    window.set_default_size(800, 600)

    webview = webkit.WebView()
    webview.connect("load-finished", load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
