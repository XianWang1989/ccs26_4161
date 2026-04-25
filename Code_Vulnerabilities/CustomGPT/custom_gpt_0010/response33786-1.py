
import gtk
import webkit

def on_load_finished(webview, frame):
    # Ensure the frame is the main frame
    if frame.get_name() == "":
        dom_document = frame.get_dom_document()
        print(dom_document)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load finished signal
    webview.connect("load-finished", on_load_finished)

    # Load a web page
    webview.load_uri("http://example.com")

    # Set up the window
    window.add(webview)
    window.set_default_size(800, 600)
    window.connect("destroy", gtk.main_quit)

    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
