
import gtk
import webkit

def get_dom(webview, frame):
    # Execute JavaScript to retrieve the DOM content
    webview.execute_script("document.documentElement.outerHTML", get_dom_callback)

def get_dom_callback(result):
    # This callback gets called with the result of the executed script
    print("DOM content:")
    print(result)

def load_finished(webview, frame):
    print("Page loaded!")
    get_dom(webview, frame)

def main():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    webview = webkit.WebView()
    # Connect the load-finished signal
    webview.connect("load_finished", load_finished)

    # Load a page
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
