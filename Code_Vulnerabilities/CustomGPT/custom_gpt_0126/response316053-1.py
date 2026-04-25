
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.update()  # Initial update
        self.parent.add(self.gtkwidget)  # Add the label to the parent

        # Schedule the update function every second
        Gdk.threads_add_idle(self.run_update)

    def run_update(self):
        self.update()
        return True  # Return True to continue calling this function

    def update(self):
        new_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(new_time)
        self.gtkwidget.queue_draw()  # Requests a redraw

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.connect("destroy", Gtk.main_quit)

        # Create clock widgets from configuration
        self.clock1 = Clock(self, "Clock1", "%H:%M:%S")
        self.clock2 = Clock(self, "Clock2", "%H:%M")

        self.show_all()  # Show all widgets

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
