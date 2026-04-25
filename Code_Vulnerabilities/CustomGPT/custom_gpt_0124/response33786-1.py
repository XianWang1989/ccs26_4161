
import gtk
import webkit

def on_load_finished(webview, frame):
    # Use JavaScript to get the whole DOM as a string
    script = "document.documentElement.outerHTML;"
    frame.evaluate(script, get_dom)

def get_dom(result):
    # This will print the HTML content of the page
    print("DOM content:", result)

def main():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)

    webview = webkit.WebView()
    webview.connect("load-finished", on_load_finished)

    # Load a page
    webview.load_uri("https://www.example.com")

    window.add(webview)
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()
