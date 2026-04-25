import gtk
import webkit

def on_load_finished(webview, frame):
    # Access the DOMDocument
    dom_document = frame.get_dom_document()
    if dom_document:
        body = dom_document.getElementsByTagName("body").item(0)
        print("Body innerHTML:")
        print(body.innerHTML)

window = gtk.Window()
webview = webkit.WebView()
webview.connect("load-finished", on_load_finished)

window.add(webview)
window.show_all()

webview.load_uri("https://example.com")

gtk.main()
