
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
import Defaults.widget
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, parent, name):
        super().__init__()
        self.parent = parent
        self.format = Defaults.widget.defaultClockFormat
        self.set_name(name)
        self.connect("destroy", self.on_destroy)
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        new_time = strftime(self.format, gmtime())
        self.set_text(new_time)
        return True  # Returning True to keep the timeout active

    def on_destroy(self, widget):
        print(f"{self.get_name()} destroyed")

# Example of parent window class
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(self.clock1, True, True, 0)
        vbox.pack_start(self.clock2, True, True, 0)

        self.add(vbox)
        self.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win = MainWindow()
    win.show_all()
    Gtk.main()
