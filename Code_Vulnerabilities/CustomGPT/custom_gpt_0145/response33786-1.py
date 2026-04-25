
import gtk
import webkit

def on_load_finished(web_view, frame):
    # This will execute JavaScript to get the DOM content
    script = "document.documentElement.outerHTML;"
    web_view.evaluate_script(script, callback)

def callback(result):
    # 'result' contains the HTML of the DOM
    print("DOM Content:")
    print(result)

def main():
    window = gtk.Window()
    web_view = webkit.WebView()

    # Connect the load-finished signal
    web_view.connect("load-finished", on_load_finished)

    # Load a URL
    web_view.load_uri("http://example.com")

    # Add the web view to the window
    window.add(web_view)
    window.show_all()

    # Start the GTK main loop
    gtk.main()

if __name__ == "__main__":
    main()
