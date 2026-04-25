
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.parent.add(self.gtkwidget)

        # Schedule the update function to be called every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw
        return True  # Keep the timeout running

# Parent window class
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        clock1 = Clock(self, "Clock1")
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
