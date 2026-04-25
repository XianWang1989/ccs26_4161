
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.gtkwidget = Gtk.Label()
        self.format = format
        self.name = name
        self.gtkwidget.set_name(name)
        self.parent = parent

        # Schedule the update function to be called every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        # Return True to keep the timeout active
        return True

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        # Create and add the Clock widget
        self.clock1 = Clock(self, "Clock1")

        # Add the clock widget to the main window
        self.add(self.clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
