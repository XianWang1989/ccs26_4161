
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name("clock_label")

        # Call update every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True to keep the timeout active

    def widget(self):
        return self.gtkwidget

# Example usage
window = Gtk.Window()
clock = Clock(window)
window.add(clock.widget())
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
