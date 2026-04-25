
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock():
    def __init__(self, parent, name):
        self.parent = parent  # Storing parent reference
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Initial format
        self.name = f"{name}_clock"
        self.gtkwidget.set_name(self.name)

        # Schedule the first update
        GLib.timeout_add_seconds(1, self.update)  

    def update(self):
        # Updating the displayed time
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

        # Ensure the label is redrawn
        self.gtkwidget.queue_draw()
        return True  # Return True to continue calling the function

    def set_format(self, new_format):
        self.format = new_format

    def widget(self):
        return self.gtkwidget
