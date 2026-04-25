
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.show_all()
        GLib.timeout_add_seconds(1, self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        return True  # Keep the timer running

    def get_clock_widget(self, name):
        return self.get_widget(name)

    def get_widget(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.format = "%H:%M:%S"

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw

    def widget(self):
        return self.gtkwidget
