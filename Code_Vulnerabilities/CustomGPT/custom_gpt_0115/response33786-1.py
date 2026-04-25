
import gtk
import webkit

def load_finished(webview, frame):
    # Execute a script to get the DOM
    script = "document.documentElement.outerHTML;"
    webview.evaluate_script(script, callback)

def callback(result, error):
    if error:
        print("Error:", error)
    else:
        print("DOM HTML:", result)

def main():
    window = gtk.Window()
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)

    webview = webkit.WebView()
    webview.connect("load_finished", load_finished)
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
