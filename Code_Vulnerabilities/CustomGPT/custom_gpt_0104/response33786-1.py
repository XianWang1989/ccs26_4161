
import gtk
import webkit

def on_load_finished(webview, frame):
    # JavaScript to get the HTML content of the body
    js_script = "document.documentElement.outerHTML"

    # Evaluate the JavaScript and get the DOM content
    frame.evaluate_script(js_script, callback=on_script_result)

def on_script_result(result):
    print("DOM content after page load:\n", result)

def main():
    # Create the GTK window
    window = gtk.Window()
    window.set_size_request(800, 600)

    # Create the WebView
    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a web page
    webview.load_uri("http://example.com")

    # Add the WebView to the window and show everything
    window.add(webview)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
