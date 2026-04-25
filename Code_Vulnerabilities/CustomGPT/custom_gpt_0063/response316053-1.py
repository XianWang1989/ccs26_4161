
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent

        # Start the clock update loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout running

    def set_format(self, format_str):
        self.format = format_str

    def widget(self):
        return self.gtkwidget

# Example Gtk Application
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instance
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        # Connect to the main window delete event
        self.connect("destroy", Gtk.main_quit)

# Main execution
if __name__ == "__main__":
    window = MainWindow()
    window.show_all()
    Gtk.main()
