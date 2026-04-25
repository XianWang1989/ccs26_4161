
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime
import Defaults.widget

class Clock(Gtk.Label):
    def __init__(self, format_string):
        super().__init__()
        self.format = format_string
        self.set_name("clock_label")
        self.update_label()
        GLib.timeout_add_seconds(1, self.update_label)  # Schedule updates every second

    def update_label(self):
        self.set_text(strftime(self.format, gmtime()))
        return True  # Keep the timeout active

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Load clocks from a configuration-like structure
        self.clocks = [
            Clock("%H:%M:%S"),
            Clock("%H:%M"),
        ]

        # Add clocks to the main window
        for clock in self.clocks:
            self.add(clock)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Start the GTK application
if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
