
#!/usr/bin/env python

from gi.repository import Gtk, GObject, Gdk
from time import gmtime, strftime
import GLib

class Clock(Gtk.Label):
    __gsignals__ = {
        'update-clock': (GObject.SIGNAL_RUN_LAST, None, (str,))
    }

    def __init__(self, name):
        super(Clock, self).__init__()
        self.format = "%H:%M:%S"
        self.set_name(name)
        self.connect('update-clock', self.on_update)

    def on_update(self, widget, new_time):
        self.set_text(new_time)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.emit('update-clock', current_time)

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock("Clock1")
        self.add(self.clock1)

        self.show_all()

        # Start update loop
        GLib.timeout_add_seconds(1, self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        return True  # Keep the timeout active

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
