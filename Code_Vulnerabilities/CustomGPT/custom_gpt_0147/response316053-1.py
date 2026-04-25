
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Widget():
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.parent = parent  # Keep a reference to the parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Directly update the clock every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        # Get current time formatted
        time_text = strftime(self.format, gmtime())
        print("Setting clock text to", time_text)

        # Update the label directly
        self.gtkwidget.set_text(time_text)
        return True  # Return True to continue the timeout

    def runCommand(self, command, lineCount):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                print(f"Badly formatted command 'format': Format: format = format.\nSkipping...")
                return

            self.format = parts[1]

    def widget(self):
        return self.gtkwidget


# Create Gtk application and main window
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")

        # Layout
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        # Instantiate the Clock widget
        clock1 = Widget(self, "Clock1")
        self.box.pack_start(clock1.widget(), True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Start Gtk main loop
if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
