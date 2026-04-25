
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, name):
        super().__init__()
        self.format = "%H:%M:%S"
        self.set_name(name)
        self.set_text(strftime(self.format, gmtime()))
        GLib.timeout_add(1000, self.update)

    def update(self):
        self.set_text(strftime(self.format, gmtime()))
        return True  # Keep the timeout active

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Creating Clock widgets
        self.clock1 = Clock("Clock1")
        self.clock2 = Clock("Clock2")

        # Layout
        box = Gtk.Box(spacing=10)
        box.pack_start(self.clock1, True, True, 0)
        box.pack_start(self.clock2, True, True, 0)
        self.add(box)

        self.connect("destroy", Gtk.main_quit)

        # Show all widgets
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
