
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class ClockWidget():
    def __init__(self, parent_name, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name + parent_name
        self.gtkwidget.set_name(self.name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        GLib.timeout_add_seconds(1, self.update)

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_size_request(200, 100)
        self.clock = ClockWidget("Clock", "Clock1")  # You could also create more instances here.
        self.add(self.clock.widget())
        self.show_all()
        # Start the first update
        self.clock.update()

if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
