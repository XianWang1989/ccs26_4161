
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        # Start the timer to update the clock every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Continue calling this function

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")

        self.set_default_size(200, 100)
        self.box = Gtk.Box()
        self.add(self.box)

        self.clock = Clock(self, "ClockLabel")
        self.box.pack_start(self.clock.widget(), True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
