
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock():
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent

        # Set an update timer to refresh the clock every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw
        return True  # Keep the timer active

    def runCommand(self, command, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                print(f"Badly formatted command 'format': {command}")
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget

class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = ParentWindow()
    Gtk.main()
