
from gi.repository import WebKit

def on_load_finished(webview, frame):
    # Example JavaScript to get the DOM as a string
    js_code = "document.documentElement.outerHTML"

    # Evaluating the JavaScript to get the DOM content
    frame.evaluate_javascript(js_code, None, None, None)

# Create your WebView and connect the load-finished event
webview = WebKit.WebView()
webview.connect("load-finished", on_load_finished)

# Load a web page
webview.load_uri("http://example.com")
