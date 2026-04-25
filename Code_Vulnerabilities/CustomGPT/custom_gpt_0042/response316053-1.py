
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime, time

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.gtkwidget = Gtk.Label()
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update_interval = 1  # Update every second
        self.update_id = None  # To hold the Glib timeout ID
        self.start_update()  # Start the update loop

    def start_update(self):
        """Start updating the clock label every second."""
        self.update()  # Initial update
        self.update_id = Gdk.threads_add_timeout_seconds(self.update_interval, self.update)

    def update(self):
        """Update the clock label."""
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True for the timeout to be called again

    def widget(self):
        """Return the Gtk widget."""
        return self.gtkwidget

# Parent Window example
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and add clock widget
        clock = Clock(self, "clock1")
        self.add(clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Running the application
if __name__ == "__main__":
    Gdk.threads_init()  # Initialize Gdk threads
    win = MainWindow()
    Gtk.main()
