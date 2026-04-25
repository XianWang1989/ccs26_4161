
import gtk
import webkit

def load_finished(webview, frame):
    # JavaScript to get the DOM content
    js_code = "document.documentElement.outerHTML"

    # Evaluate the script in the web view frame
    frame.evaluate_script(js_code, callback=on_script_evaluated)

def on_script_evaluated(result, webview):
    # 'result' contains the HTML of the DOM
    print("DOM Content:")
    print(result)

# Set up the WebKit WebView
window = gtk.Window()
webview = webkit.WebView()
webview.connect("load_finished", load_finished)

# Load a webpage
webview.load_uri("http://example.com")
window.add(webview)
window.show_all()
gtk.main()
