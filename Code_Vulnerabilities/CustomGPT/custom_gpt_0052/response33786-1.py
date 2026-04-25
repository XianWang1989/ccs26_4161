
import gtk
import webkit

def on_load_finished(web_view, frame):
    # Execute JavaScript to get the DOM
    script = "document.documentElement.outerHTML"
    frame.evaluate_script(script, callback=on_dom_retrieved)

def on_dom_retrieved(result, error):
    if error:
        print("Error retrieving DOM:", error)
    else:
        print("DOM retrieved successfully:")
        print(result)

def main():
    window = gtk.Window()
    window.set_default_size(800, 600)

    web_view = webkit.WebView()
    web_view.connect('load-finished', on_load_finished)

    # Load a webpage
    web_view.load_uri("http://example.com")

    window.add(web_view)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
