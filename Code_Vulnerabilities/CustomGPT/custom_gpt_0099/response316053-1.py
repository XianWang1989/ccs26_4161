
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import output, Defaults.widget

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = Defaults.widget.defaultClockFormat
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)

        # Add the label to the parent's container
        self.parent.add(self.gtkwidget)
        self.parent.show_all()

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]
