
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib  # Import GLib for time updating

class WidgetManager(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.clock1.start_update()  # Start the update loop

        self.add(self.clock1.widget())

    def runFromChildToParent(self, label, text):
        # Directly updates the Gtk.Label's text
        label.set_text(text)
        label.queue_draw()  # Ensure label gets redrawn

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.gtkwidget.set_name(name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.parent.runFromChildToParent(self.gtkwidget, current_time)

    def widget(self):
        return self.gtkwidget

    def start_update(self):
        GLib.timeout_add(1000, self.update)  # Update every second

# Main Code to run the application
if __name__ == "__main__":
    win = WidgetManager()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
