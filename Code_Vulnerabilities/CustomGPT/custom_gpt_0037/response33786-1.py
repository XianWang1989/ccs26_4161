
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    frame.execute_script("document.documentElement.outerHTML", callback)

def callback(result):
    print("DOM content:")
    print(result)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    # Create a WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the webview to the window
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
