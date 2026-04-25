
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format='%H:%M:%S'):
        self.parent = parent
        self.format = format
        self.label = Gtk.Label()
        self.label.set_name(name)
        self.parent.add(self.label)
        self.label.show()

        # Schedule the update function to run every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        return True  # Return True to continue the timeout

    def set_format(self, new_format):
        self.format = new_format

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instances
        self.clock1 = Clock(self, "Clock1", "%H:%M:%S")
        self.clock2 = Clock(self, "Clock2", "%H:%M")

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MyWindow()
    Gtk.main()
