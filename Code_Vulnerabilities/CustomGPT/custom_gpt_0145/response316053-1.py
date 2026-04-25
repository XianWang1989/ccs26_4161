
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name("clock_label")
        self.update()  # Set initial time
        GLib.timeout_add_seconds(1, self.update)  # Call update every second

    def update(self):
        time_string = strftime(self.format, gmtime())
        self.gtkwidget.set_text(time_string)
        # Optional: Force a redraw, generally not needed
        self.gtkwidget.queue_draw()
        return True  # Return True to keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.set_border_width(10)

        self.clock = Clock(self)  # Pass parent to Clock
        self.add(self.clock.widget())

if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
