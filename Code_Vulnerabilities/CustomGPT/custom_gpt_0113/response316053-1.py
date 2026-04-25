
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.label = Gtk.Label()
        self.label.set_name(self.name)

        # Set a timeout to update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.label.set_text(current_time)
        self.label.queue_draw()  # Ensure the label redraws
        return True  # Return True to continue the timeout

    def get_widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create clocks based on configuration
        clock1 = Clock(self, "Clock1")
        clock2 = Clock(self, "Clock2")

        # Pack widgets into the window
        self.add(clock1.get_widget())
        self.add(clock2.get_widget())

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
