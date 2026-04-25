
import gtk
import webkit

def load_finished(webview, frame):
    # JavaScript to get the document's HTML
    script = "document.documentElement.innerHTML"
    webview.execute_script(script)

def evaluation_result(webview, result):
    # This function captures the result of the JavaScript evaluation
    print("DOM Content:", result)

def main():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load_finished event
    webview.connect("load-finished", load_finished)

    # Connect the JavaScript evaluation result callback
    webview.connect("evaluate-javascript-finished", evaluation_result)

    # Load a webpage
    webview.load_uri("http://example.com")
    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
