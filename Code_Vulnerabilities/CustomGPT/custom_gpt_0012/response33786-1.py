
import gtk
import webkit

def on_load_finished(webview, event):
    # Execute JavaScript to get the DOM content
    webview.execute_script("document.documentElement.innerHTML = document.documentElement.outerHTML;")
    # You can add additional logic here to process the DOM content.

def create_webview():
    window = gtk.Window()
    webview = webkit.WebView()

    # Connect to the load_finished signal
    webview.connect("load-finished", on_load_finished)

    # Load a webpage
    webview.load_url("https://example.com")

    window.add(webview)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    create_webview()
