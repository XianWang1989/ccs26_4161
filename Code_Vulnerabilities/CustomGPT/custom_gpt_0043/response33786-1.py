
import gtk
import webkit

def on_load_finished(webview, frame):
    # Define the JavaScript that retrieves the DOM content
    js_code = "document.documentElement.outerHTML;"

    # Evaluate the JavaScript and get the DOM content
    frame.evaluate_script(js_code)

    # Connect to the script's evaluation callback
    frame.connect("evaluate-javascript-response", on_evaluate_response)

def on_evaluate_response(frame, script, result, user_data):
    if result:
        print("DOM content retrieved:")
        print(result)

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_title("WebKit Example")
    window.set_size_request(800, 600)

    # Create a WebView
    webview = webkit.WebView()

    # Connect the "load-finished" signal to the callback
    webview.connect("load-finished", on_load_finished)

    # Load a URL
    webview.load_uri("https://www.example.com")

    # Add the WebView to the window
    window.add(webview)

    # Show the window and WebView
    window.show_all()

    # Main GTK loop
    gtk.main()

if __name__ == "__main__":
    main()
