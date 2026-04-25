
import webkit

def on_load_finished(webview, frame):
    # This will be called when the page has finished loading
    javascript = "document.documentElement.outerHTML"

    # Use evaluate_script to get the DOM
    frame.evaluate_script(javascript, completion_handler=dom_retrieved)

def dom_retrieved(result, error):
    if error:
        print("Error retrieving DOM:", error)
    else:
        print("DOM retrieved successfully!")
        print(result)  # This will contain the HTML of the loaded page

# Create your webview and connect to the load-finished event
webview = webkit.WebView()
webview.load_finished.connect(on_load_finished)

# Load a webpage
webview.load_url("https://example.com")
