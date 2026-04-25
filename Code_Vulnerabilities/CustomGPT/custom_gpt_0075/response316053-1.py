
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.name = name
        self.gtkwidget.set_name(name)
        self.start_update()

    def start_update(self):
        # Use GLib.timeout_add to call the update method periodically
        GLib.timeout_add(1000, self.update)

    def update(self):
        # Update the clock label every second
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout active

    def get_widget(self):
        return self.gtkwidget
