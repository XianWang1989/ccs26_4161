
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib  # for timeout_add

class Clock:
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default clock format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent  # Keep reference to the parent

        # Initialize the clock update every second
        GLib.timeout_add(1000, self.update)  # Update every 1000 milliseconds (1 second)

    def update(self):
        # Update the clock text
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        return True  # Return True to keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_border_width(10)

        # Here, we can add more clocks from configuration
        clock1 = Clock(self, "Clock1")
        self.add(clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Run the application
if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
