
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.format = "%H:%M:%S"  # Default format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw to ensure updates
        return True  # To keep the timer running

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(300, 200)
        self.connect("destroy", Gtk.main_quit)

        # Create clocks based on configuration
        clock1 = Clock(self, "Clock1")
        clock2 = Clock(self, "Clock2")

        self.show_all()  # Show all widgets

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
