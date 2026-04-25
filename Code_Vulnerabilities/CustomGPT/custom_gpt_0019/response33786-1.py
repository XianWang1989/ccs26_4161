
import sys
from gi.repository import WebKit, Gtk

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM content
    webview.execute_script("document.documentElement.outerHTML", callback)

def callback(result):
    print("DOM Content:")
    print(result)

def main():
    window = Gtk.Window()
    webview = WebKit.WebView()

    # Connect the load-finished signal
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Set up the Gtk window
    window.add(webview)
    window.set_default_size(800, 600)
    window.connect("destroy", Gtk.main_quit)
    window.show_all()

    Gtk.main()

if __name__ == "__main__":
    main()
