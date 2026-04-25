
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Setup a GLib timeout to update every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensure the widget is redrawn
        return True  # To continue the timeout

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]
            self.update()  # Update immediately after changing the format

    def widget(self):
        return self.gtkwidget
