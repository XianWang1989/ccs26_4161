
#!/usr/bin/env python

from gi.repository import Gtk, GObject
from time import gmtime, strftime

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name("ClockLabel")

        # Schedule the update method to run every second
        GObject.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Returning True to continue timeout

    def widget(self):
        return self.gtkwidget

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a clock and add its widget to the window
        self.clock = Clock(self)
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MyWindow()
    Gtk.main()
