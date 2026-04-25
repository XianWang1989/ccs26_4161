
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Widget():
    def __init__(self, parent, name):
        self.parent = parent  
        self.gtkwidget = Gtk.Label() 
        self.format = "%H:%M:%S"  
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Add the widget to the parent
        parent.add(self.gtkwidget)  
        parent.show_all()

        # Start the update timer
        GLib.timeout_add(1000, self.update)  

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)  
        self.gtkwidget.queue_draw()  # Request a redraw
        return True  # Keep the timeout going

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

# Example parent class
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Initialize Clock widget
        clock = Widget(self, "Clock1")

    def on_destroy(self, widget):
        Gtk.main_quit()

def main():
    window = MainWindow()
    window.connect("destroy", window.on_destroy)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
