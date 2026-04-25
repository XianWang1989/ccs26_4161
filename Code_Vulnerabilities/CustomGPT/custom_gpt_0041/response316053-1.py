
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, name, format="%H:%M:%S"):
        super().__init__()
        self.set_name(name)
        self.format = format
        self.update_clock()
        GLib.timeout_add_seconds(1, self.update_clock)

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        self.set_text(current_time)
        return True  # Return True to continue calling this function

# Main application
class MainWin(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock("Clock1", "%H:%M:%S")
        self.clock2 = Clock("Clock2", "%H:%M")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(self.clock1, True, True, 0)
        box.pack_start(self.clock2, True, True, 0)

        self.add(box)
        self.connect("destroy", Gtk.main_quit)

# Run the application
if __name__ == "__main__":
    win = MainWin()
    win.show_all()
    Gtk.main()
