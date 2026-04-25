
import gtk
import webkit

def on_load_finished(webview, frame):
    # Use evaluate_script to fetch the DOM
    js_code = "document.documentElement.outerHTML"
    webview.evaluate_script(js_code, done_callback)

def done_callback(result):
    # This function will handle the result of the script execution
    print("DOM content:")
    print(result)

# Create the WebKit WebView
webview = webkit.WebView()
webview.connect("load-finished", on_load_finished)

# Load a URL
webview.load_uri("http://example.com")

# Start the GTK main loop
gtk main()

