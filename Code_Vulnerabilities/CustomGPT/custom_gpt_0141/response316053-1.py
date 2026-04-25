
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, name, format="%H:%M:%S"):
        super().__init__()
        self.set_name(name)
        self.format = format
        self.update()  # Set initial time
        GLib.timeout_add_seconds(1, self.update)  # Schedule to update every second

    def update(self):
        self.set_text(strftime(self.format, gmtime()))
        return True  # Keep the timeout callback active

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Read clocks from configuration and create Clock instances
        self.create_clocks()

    def create_clocks(self):
        clock1 = Clock("Clock1", "%H:%M:%S")
        clock2 = Clock("Clock2", "%H:%M")  # Different format
        self.grid.attach(clock1, 0, 0, 1, 1)
        self.grid.attach(clock2, 0, 1, 1, 1)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
