
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import gi
gi.require_version("Gtk", "3.0")

class WidgetManager(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Manager")
        self.set_default_size(300, 200)
        self.clocks = []

        # Initialize Clocks based on configuration
        self.load_clocks()

        # Start a timer to update the clocks every second
        GLib.timeout_add(1000, self.update_clocks)

    def load_clocks(self):
        # Example clocks creation based on configuration
        clock1 = Clock(self, "Clock1")
        clock2 = Clock(self, "Clock2")
        self.clocks.extend([clock1, clock2])

        # Add clocks to the window
        for clock in self.clocks:
            self.add(clock.widget())

    def update_clocks(self):
        for clock in self.clocks:
            clock.update()
        return True  # Keep the timer running

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

    def widget(self):
        return self.gtkwidget

# Run the application
win = WidgetManager()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
