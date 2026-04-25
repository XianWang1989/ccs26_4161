
import gi
gi.require_version('WebKit', '4.0')
from gi.repository import WebKit, Gtk

def load_finished(webview, frame):
    # This will execute when the page finishes loading
    script = "document.documentElement.outerHTML"
    webview.run_javascript(script, None, on_javascript_finished, None)

def on_javascript_finished(result, exception):
    if exception is None:
        print("DOM Content:")
        print(result)  # This will print the HTML content of the loaded page
    else:
        print("Error running JavaScript:", exception)

def main():
    win = Gtk.Window()
    webview = WebKit.WebView()

    # Connect the load-finished event to the callback function
    webview.connect("loadFinished", load_finished)

    # Load a webpage
    webview.load_uri("https://example.com")

    win.add(webview)
    win.connect("destroy", Gtk.main_quit)
    win.set_default_size(800, 600)
    win.show_all()

    Gtk.main()

if __name__ == "__main__":
    main()
