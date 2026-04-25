
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start a timeout to update the clock every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensure the widget is redrawn
        return True  # Return True to continue the timeout

    def runCommand(self, command, lineCount):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1]
            else:
                print(f"Badly formatted command at line {lineCount}")

    def widget(self):
        return self.gtkwidget

# Example parent usage
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instance
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
