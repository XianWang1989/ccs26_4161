
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import output, Defaults.widget

class Clock:
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.parent = parent  # Store reference to the parent
        self.gtkwidget = Gtk.Label()  # Gtk Widget
        self.format = Defaults.widget.defaultClockFormat
        self.name = name + "_clock"  # Ensure uniqueness
        self.gtkwidget.set_name(self.name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)  # Updating label directly
        self.gtkwidget.queue_draw()  # Request a redraw to ensure visibility

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                output.stderr(
                    f"{configurationFile}, line {lineCount}: Badly formatted command 'format': Format: format = format.\nSkipping..."
                )
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget
