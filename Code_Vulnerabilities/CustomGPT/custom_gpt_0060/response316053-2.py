
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start the update timer
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True to continue the timer

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")

        self.set_size_request(200, 100)
        self.connect("destroy", Gtk.main_quit)

        # Adding a Clock widget
        clock = Clock(self, "Clock1")
        self.add(clock.widget())

        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
