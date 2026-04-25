
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    dom_content = webview.evaluate_js("document.documentElement.outerHTML")
    print(dom_content)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect to the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("https://www.example.com")

    # Set up the window and show it
    window.add(webview)
    window.connect("destroy", gtk.main_quit)
    window.set_default_size(800, 600)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
