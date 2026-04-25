
#!/usr/bin/env python

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        # Start the update loop every 1000 milliseconds (1 second)
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request redraw if necessary
        return True  # Keep the timeout running

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        # Clock widget instance
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        # Option to close the window
        self.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    win = MainWindow()
    win.show_all()
    Gtk.main()
