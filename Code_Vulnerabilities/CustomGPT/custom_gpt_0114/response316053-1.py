
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import Defaults.widget

class Clock:
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.format = Defaults.widget.defaultClockFormat
        self.gtkwidget = Gtk.Label()
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent  # Keep a reference to the parent

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)

        # Set text for the widget
        self.gtkwidget.set_text(current_time)

        # Ensure the widget is drawn
        self.gtkwidget.queue_draw()

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget
