
import gtk
import webkit

def webview_load_finished(webview, frame):
    # Use evaluateJavaScript to get the DOM
    script = 'document.documentElement.outerHTML'
    webview.evaluate_java_script(script, frame)

def on_js_result(webview, js_result, frame):
    # Handle the result from the JavaScript execution
    print(js_result)

# Create a WebView and connect signals
webview = webkit.WebView()
webview.connect("load-finished", webview_load_finished)
webview.connect("js-result", on_js_result)

# Load a web page
webview.load_uri("http://example.com")

# Show the WebView
window = gtk.Window()
window.add(webview)
window.show_all()
gtk.main()
