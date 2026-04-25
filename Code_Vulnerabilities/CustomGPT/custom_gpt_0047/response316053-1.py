
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.name = name
        self.label = Gtk.Label()
        self.label.set_name(name)
        self.parent.add(self.label)

        # Start the update loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        if self.label.get_text() != current_time:
            self.label.set_text(current_time)
            self.label.queue_draw()  # Request a redraw
        return True  # Keep the timeout active

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")
        self.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
