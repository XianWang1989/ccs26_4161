
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib

class Clock(Gtk.Label):
    def __init__(self, name):
        super().__init__()
        self.format = "%H:%M:%S"
        self.set_name(name)
        self.set_text(strftime(self.format, gmtime()))
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        self.set_text(strftime(self.format, gmtime()))
        return True  # Keep the timeout active

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_size_request(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        # Create clocks
        clock1 = Clock("Clock1")
        clock2 = Clock("Clock2")

        vbox.pack_start(clock1, True, True, 0)
        vbox.pack_start(clock2, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MyWindow()
    Gtk.main()
