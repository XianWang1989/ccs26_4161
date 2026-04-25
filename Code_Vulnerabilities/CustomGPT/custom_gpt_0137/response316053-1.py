
#!/usr/bin/env python
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        parent.add(self.gtkwidget)

        # Start the timer that updates the clock every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        # Update the label text with the current time
        self.gtkwidget.set_text(strftime(self.format, gmtime()))
        self.gtkwidget.queue_draw()  # Request a redraw of the widget
        return True  # Continue calling this function

    def runCommand(self, command):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                print("Badly formatted command: Format: format=format.")
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        self.clock1 = Clock(self, "Clock1")

        # Show widgets
        self.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
