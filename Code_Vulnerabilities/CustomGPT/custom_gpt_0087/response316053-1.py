
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Schedule the update method to be called every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Continue calling this function

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(250, 150)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.show_all()

if __name__ == "__main__":
    Gtk.init()
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
