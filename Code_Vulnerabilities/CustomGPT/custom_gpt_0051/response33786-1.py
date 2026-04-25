
import gtk
import webkit

def on_load_finished(web_view, frame):
    # This callback runs when the page has finished loading
    if frame.get_name() == "":
        # Execute JavaScript to get the DOM
        script = "document.documentElement.outerHTML"
        web_view.execute_script(script, callback)

def callback(result):
    # This function is called with the result of the executed script
    print("DOM Content Retrieved:")
    print(result)  # result contains the HTML content of the page

def main():
    # Create a GTK window
    window = gtk.Window()
    window.set_title("WebKit Example")
    window.set_size_request(800, 600)

    # Create a WebView
    web_view = webkit.WebView()
    web_view.connect("load-finished", on_load_finished)

    # Load a web page
    web_view.load_uri("https://www.example.com")

    # Add the WebView to the window
    window.add(web_view)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
