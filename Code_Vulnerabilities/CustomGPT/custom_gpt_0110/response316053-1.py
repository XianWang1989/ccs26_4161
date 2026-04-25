
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib  # For timeout functionality

class Clock(Gtk.Label):
    def __init__(self, name, format):
        super().__init__()
        self.format = format
        self.set_name(name)
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.set_text(current_time)
        return True  # Keep the timeout active

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and pack the clock widgets
        clock1 = Clock("Clock1", "%H:%M:%S")
        clock2 = Clock("Clock2", "%H:%M")

        self.add(Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6).pack_start(clock1, True, True, 0))
        self.add(Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6).pack_start(clock2, True, True, 0))

    def get_clock_by_name(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
