
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import gi
gi.require_version('Gdk', '3.0')

class Clock(Gtk.Box):
    def __init__(self, format="%H:%M:%S", **kwargs):
        super().__init__(**kwargs)
        self.label = Gtk.Label()
        self.format = format
        self.pack_start(self.label, True, True, 0)

        # Set the label name for access
        self.label.set_name("clock_label")

        # Start the update timer
        self.update_clock()

    def update_clock(self):
        # Updates the label text with the current time
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)

        # Schedule the next update in 1 second
        Gdk.threads_add_idle(self.update_clock)

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and add clock widget
        self.clock = Clock()
        self.add(self.clock)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Gdk.threads_init()  # Initialize threads
    win = MainWindow()
    Gtk.main()
