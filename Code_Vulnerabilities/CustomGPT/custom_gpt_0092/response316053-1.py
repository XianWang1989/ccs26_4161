
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.name = name
        self.format = format

        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.update()

        # Schedule the update every second
        GLib(timeout_add_seconds(1, self.update))

    def update(self):
        # Update the clock label
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

        # Optionally, ensure the widget is redrawn
        self.gtkwidget.queue_draw()

    def widget(self):
        return self.gtkwidget


class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")

        # Storing Clock instances
        self.clocks = []

        # Create Clock instances
        clock1 = Clock(self, "clock1", format="%H:%M:%S")
        clock2 = Clock(self, "clock2", format="%H:%M")

        self.add(clock1.widget())
        self.add(clock2.widget())

        # Set the window properties
        self.set_default_size(200, 100)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    win = ParentWindow()
    Gtk.main()
