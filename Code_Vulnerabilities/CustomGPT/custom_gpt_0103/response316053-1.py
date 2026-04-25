
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.format = "%H:%M:%S"  # Default format
        self.parent = parent
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)

        # Add the label to the parent's layout (assumes VBox or similar)
        self.parent.add(self.gtkwidget)

        # Schedule the update method to be called every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        # Get current time formatted
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw
        return True  # Continue calling this function

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1].strip()

    def widget(self):
        return self.gtkwidget
