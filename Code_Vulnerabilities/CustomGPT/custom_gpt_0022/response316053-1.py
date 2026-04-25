
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent

        # Start a timer to update the clock every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw
        return True  # Return True to keep the timer active

    def widget(self):
        return self.gtkwidget

class MyApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(250, 100)

        # Create a Clock instance
        clock = Clock(self, "Clock1")
        self.add(clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

app = MyApp()
Gtk.main()
