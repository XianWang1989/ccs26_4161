
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.label = Gtk.Label()
        self.label.set_name(name)
        self.format = format
        self.update()

        # Schedule updates every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        return True  # Return True to continue the timeout

    def widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock widgets based on some configuration
        clock1 = Clock(self, "Clock1", format="%H:%M:%S")
        clock2 = Clock(self, "Clock2", format="%H:%M")

        # Add widgets to the window
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(clock1.widget(), True, True, 0)
        box.pack_start(clock2.widget(), True, True, 0)
        self.add(box)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
