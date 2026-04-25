
import gtk
import webkit

def on_load_finished(webview, frame):
    # Check if the frame is the main frame
    if frame == webview.get_main_frame():
        # JavaScript to get the DOM content
        js_code = "document.documentElement.outerHTML"
        # Evaluate JavaScript
        webview.evaluate_javascript(js_code, on_javascript_evaluated)

def on_javascript_evaluated(webview, result):
    # This callback will have the result of the JavaScript execution
    print("DOM content:")
    print(result)  # You can process the result as needed

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect to the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.set_size_request(800, 600)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()
