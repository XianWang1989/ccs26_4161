
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.update_label()  # Initial update

        # Set up a timeout to update the label every second
        GLib.timeout_add(1000, self.update)  # Update every 1000 ms

    def update(self):
        self.update_label()
        return True  # Return True to continue the timeout

    def update_label(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

    def widget(self):
        return self.gtkwidget


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Clock Example")
        self.set_default_size(200, 100)
        self.connect("destroy", Gtk.main_quit)

        # Create instances of Clock
        clock1 = Clock(self, "Clock1", format="%H:%M:%S")
        clock2 = Clock(self, "Clock2", format="%H:%M")

        # Pack the clock widgets into the window
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(clock1.widget(), True, True, 0)
        vbox.pack_start(clock2.widget(), True, True, 0)

        self.add(vbox)
        self.show_all()


if __name__ == "__main__":
    win = MyWindow()
    Gtk.main()
