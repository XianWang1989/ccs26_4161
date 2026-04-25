
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.parent.add(self.gtkwidget)
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force a redraw if necessary
        return True  # Keep the timeout active

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2", format="%H:%M")

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Create and run the main application
win = MainWindow()
Gtk.main()
