
import gtk
import webkit

def load_finished(web_view, frame):
    # JavaScript code to get the entire DOM as a string
    js_code = "new XMLSerializer().serializeToString(document);"

    # Execute the JavaScript code in the context of the given frame
    frame.evaluate_script(js_code)

# Function to handle the output of the executed script
def on_script_result(web_view, frame, result):
    print("The DOM content is:")
    print(result)

# Create a new GTK window and WebView
window = gtk.Window()
web_view = webkit.WebView()

# Connect the 'load-finished' signal to our callback function
web_view.connect('load-finished', load_finished)

# Connect to the signal to receive the result
web_view.connect('script-contacted', on_script_result)

# Load a webpage
web_view.load_uri("https://www.example.com")

# Add the WebView to the window and show everything
window.add(web_view)
window.show_all()

# Start the GTK main loop
gtk.main()
