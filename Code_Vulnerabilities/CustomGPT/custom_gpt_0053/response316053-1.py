
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start the update timer
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timer running

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create the Clock widget
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())
        self.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    window = MainWindow()
    window.show_all()
    Gtk.main()
