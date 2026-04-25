
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import signal

class Clock:
    def __init__(self, parent, name):
        # Store parent and widget name
        self.parent = parent
        self.name = name
        self.format = "%H:%M:%S"  # default format

        # Create and name the Gtk.Label widget
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)

    def update(self):
        # Update the label text
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw

    def run_command(self, command):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1]

class MyApplication(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instances
        self.clocks = [
            Clock(self, "Clock1"),
            Clock(self, "Clock2")
        ]

        # Update clocks every second
        self.timeout_id = Gdk.timeout_add(1000, self.update_clocks)

    def update_clocks(self):
        for clock in self.clocks:
            clock.update()
        return True  # Keep the timeout active

def main():
    app = MyApplication()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
