
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime
import Defaults.widget

class Clock():
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Schedule the update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)  # Update label text
        return True  # Return True to keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Adding Clock widget
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    MainWindow()
    Gtk.main()
