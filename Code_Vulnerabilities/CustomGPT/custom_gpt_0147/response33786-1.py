
from gi.repository import WebKit, Gtk

def on_load_finished(webview, frame):
    # Check if the frame is valid
    if frame is not None:
        # Evaluate JavaScript to get DOM content
        webview.evaluate("document.documentElement.outerHTML", lambda result, error: handle_result(result, error))

def handle_result(result, error):
    if error:
        print("Error occurred: ", error)
    else:
        print("DOM Content: ", result)

# Initialize the GTK application
def main():
    window = Gtk.Window()
    webview = WebKit.WebView()

    # Connect the load finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
