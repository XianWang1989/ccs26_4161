
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start updating the clock every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Continue the timeout

    def widget(self):
        return self.gtkwidget


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and add Clock widgets
        clock1 = Clock(self, "Clock1")
        self.add(clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    win = MyWindow()
    Gtk.main()
