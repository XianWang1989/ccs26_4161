
from gi.repository import Gtk, GLib

class WidgetManager:
    def __init__(self):
        self.clock = Clock(self)

        # Start the update timer
        GLib.timeout_add(1000, self.update_clocks)

    def update_clocks(self):
        self.clock.update()
        return True  # Keep the timer running

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name("ClockLabel")

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
