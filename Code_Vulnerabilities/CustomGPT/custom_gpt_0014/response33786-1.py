
import gtk
import webkit

def on_load_finished(webview, frame):
    # JavaScript to get the entire HTML document
    js_code = "document.documentElement.outerHTML"

    # Execute the script and get the result
    frame.evaluate_script(js_code)

    # To handle the result asynchronously
    frame.connect("evaluate-completed", on_evaluate_completed)

def on_evaluate_completed(frame, result, _):
    html_content = result.get_data()
    print("HTML content loaded:")
    print(html_content)

def main():
    # Set up the GTK window and WebView
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect the load-finished event
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_uri("http://example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
