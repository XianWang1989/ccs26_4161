
#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
from time import strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.label = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.label.set_name(name)
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        current_time = strftime(self.format)
        self.label.set_text(current_time)
        return True  # Keep the timeout active

    def get_widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(300, 100)

        # Create Clock instances
        self.clocks = [
            Clock(self, "Clock1"),
            Clock(self, "Clock2"),
        ]

        # Pack the Clock widgets into the window
        for clock in self.clocks:
            self.add(clock.get_widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
