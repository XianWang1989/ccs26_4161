
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.format = "%H:%M:%S"

        # Start the update loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True to keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        clock = Clock(self, "ClockLabel")
        self.add(clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

win = MainWindow()
Gtk.main()
