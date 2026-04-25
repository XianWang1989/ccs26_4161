
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.label = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.label.set_name(name)
        self.start_timer()

    def start_timer(self):
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        return True  # Keep the timeout active

    def widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
