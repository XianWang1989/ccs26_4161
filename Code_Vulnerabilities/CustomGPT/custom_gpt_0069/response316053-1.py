
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.format = "%H:%M:%S"  # Default format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        # Start updating the clock every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True to continue calling this function

    def widget(self):
        return self.gtkwidget

    def runCommand(self, command):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1].strip()

# Parent Window Example
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        hbox = Gtk.Box(spacing=10)
        self.add(hbox)

        # Create a Clock widget
        clock_widget = Clock(self, "Clock1").widget()
        hbox.pack_start(clock_widget, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Run the application
if __name__ == "__main__":
    win = MyWindow()
    Gtk.main()
