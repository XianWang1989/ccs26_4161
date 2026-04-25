
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        parent.add(self.gtkwidget)  # Add label to parent widget

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

# Example Parent Window
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.connect("destroy", Gtk.main_quit)

        # Create Clock widgets
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        self.show_all()

    def update_clocks(self):
        self.clock1.update()
        self.clock2.update()

# Main event loop
win = MainWindow()

# Update every second
def on_timeout():
    win.update_clocks()
    return True

Gdk.threads_add_idle(Gdk.PRIORITY_DEFAULT, on_timeout)

Gtk.main()
