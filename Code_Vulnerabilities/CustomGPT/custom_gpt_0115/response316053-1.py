
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        # Add the widget to the parent container
        self.parent.add(self.gtkwidget)
        self.update_timer()

    def update(self):
        time_text = strftime(self.format, gmtime())
        self.gtkwidget.set_text(time_text)

    def update_timer(self):
        # Call update every second
        GLib.timeout_add_seconds(1, self.update)

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock widget
        self.clock1 = Clock(self, "Clock1")

        self.show_all()

# Start the GTK application
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
