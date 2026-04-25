
import webkit

def on_load_finished(webview, frame):
    # Execute JavaScript to get the DOM
    frame.evaluate_script("document.documentElement.outerHTML", 
                          callback=on_dom_received)

def on_dom_received(dom):
    # This function receives the DOM as a string
    print("DOM content:")
    print(dom)

# Set up the WebView
webview = webkit.WebView()
webview.connect("load-finished", on_load_finished)

# Load a webpage
webview.load_uri("http://example.com")
