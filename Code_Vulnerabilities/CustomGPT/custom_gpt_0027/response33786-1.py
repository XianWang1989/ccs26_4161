
import gtk
import webkit

def load_finished(webview, frame):
    # This function is called when the page has loaded
    print("Page loaded!")
    # Execute JavaScript to retrieve the DOM
    js_code = "document.documentElement.outerHTML"
    frame.evaluate_script(js_code)

def on_eval_script_finished(webview, frame, result):
    # This function handles the result of the executed script
    print("DOM Content: ", result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished signal to the callback
    webview.connect("load_finished", load_finished)

    # Connect the script evaluation signal
    webview.connect("evaluate_script_finished", on_eval_script_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    # Add the WebView to the window and show it
    window.add(webview)
    window.set_default_size(800, 600)
    window.connect("destroy", gtk.main_quit)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
