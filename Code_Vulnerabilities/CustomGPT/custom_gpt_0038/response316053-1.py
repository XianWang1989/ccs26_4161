
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime, sleep

class Clock(Gtk.Label):
    def __init__(self, format="%H:%M:%S", name="ClockLabel"):
        super().__init__()
        self.format = format
        self.set_name(name)
        self.update_label()

        # Set a timeout to update the label every second
        Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT, self.update_label)

    def update_label(self):
        self.set_text(strftime(self.format, gmtime()))
        return True  # Keep timeout running

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_border_width(10)

        # Create two clock widgets
        self.clock1 = Clock(format="%H:%M:%S", name="Clock1")
        self.clock2 = Clock(format="%H:%M", name="Clock2")

        # Arrange widgets
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.pack_start(self.clock1, True, True, 0)
        box.pack_start(self.clock2, True, True, 0)

        self.add(box)

        # Show all widgets
        self.show_all()

# Running the application
def main():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()

if __name__ == "__main__":
    main()
