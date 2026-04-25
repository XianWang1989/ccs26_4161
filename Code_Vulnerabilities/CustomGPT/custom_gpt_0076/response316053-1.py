
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update_clock()  # Start the clock updates

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

        # Schedule the next update after 1 second
        GLib.timeout_add(1000, self.update_clock)
        return False  # Return False to avoid rescheduling again

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1]

    def widget(self):
        return self.gtkwidget

# Parent Widget Example
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Run the application
if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
