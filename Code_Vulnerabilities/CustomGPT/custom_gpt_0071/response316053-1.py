
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update_clock()  # Initial call to update clock
        GLib.timeout_add(1000, self.update_clock)  # Update every second

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout running

    def widget(self):
        return self.gtkwidget

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        # Create multiple Clock widgets if needed
        clock1 = Clock(self, "Clock1")
        hbox.pack_start(clock1.widget(), True, True, 0)

        clock2 = Clock(self, "Clock2")
        hbox.pack_start(clock2.widget(), True, True, 0)

        self.connect("destroy", Gtk.main_quit)

win = MyWindow()
win.show_all()
Gtk.main()
