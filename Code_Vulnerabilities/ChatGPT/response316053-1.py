
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock():
    def __init__(self, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(name)

        # Schedule the update function every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        return True  # Return True to continue the timer

    def runCommand(self, command):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                print(f"Badly formatted command '{command}'.")
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create clock widget and add to window
        self.clock = Clock("Clock1")
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

win = MainWindow()
Gtk.main()
