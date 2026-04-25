
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name("ClockWidget")
        self.gtkwidget.set_text(self.get_current_time())

        # Start the timer for updates
        GLib.timeout_add_seconds(1, self.update)

    def get_current_time(self):
        return strftime(self.format, gmtime())

    def update(self):
        self.gtkwidget.set_text(self.get_current_time())
        return True  # Return True to keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and add the clock widget
        self.clock = Clock(self)
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
