
import gtk
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    js_code = "document.documentElement.outerHTML"

    # Use the evaluate_script method to run the JS code and get the result
    frame.evaluate_script(js_code)

def on_script_finished(webview, frame, result):
    # This callback gets the result of the script execution
    print("DOM Loaded:")
    print(result)

def main():
    # Initialize GTK
    gtk.main()

    # Create a WebView
    webview = webkit.WebView()

    # Connect to the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Connect to the script-finished event to handle the result
    webview.connect("evaluate-performed", on_script_finished)

    # Load a web page
    webview.load_uri("http://example.com")

    # Show the WebView
    webview.show()

    gtk.main()

if __name__ == "__main__":
    main()
