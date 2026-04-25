
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import strftime, gmtime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.update()

        # Start the updating mechanism
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Returning True keeps the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        # Create and add clocks
        self.clock1 = Clock(self, "Clock1", format="%H:%M:%S")
        self.clock2 = Clock(self, "Clock2", format="%H:%M")

        box = Gtk.VBox()
        box.pack_start(self.clock1.widget(), True, True, 0)
        box.pack_start(self.clock2.widget(), True, True, 0)

        self.add(box)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
