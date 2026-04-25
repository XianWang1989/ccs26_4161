
import gtk
import webkit

def on_load_finished(web_view, frame):
    # Execute JavaScript to get the DOM
    web_view.run_javascript("document.documentElement.outerHTML", None, dom_ready, None)

def dom_ready(result, frame):
    # Handle the DOM content (result) here
    print("DOM content:", result)

def main():
    window = gtk.Window()
    web_view = webkit.WebView()

    web_view.connect("load-finished", on_load_finished)

    window.add(web_view)
    window.set_size_request(800, 600)
    window.connect("destroy", gtk.main_quit)

    web_view.load_uri("http://example.com")  # Replace with your desired URL
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
