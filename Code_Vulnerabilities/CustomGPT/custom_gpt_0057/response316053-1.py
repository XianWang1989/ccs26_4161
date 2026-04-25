
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import gi

gi.require_version("Gtk", "3.0")

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.parent.add(self.gtkwidget)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()

    def set_format(self, new_format):
        self.format = new_format

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.set_border_width(10)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        self.show_all()
        self.update_clocks()

    def update_clocks(self):
        self.clock1.update()
        self.clock2.update()
        Gdk.threads_add_idle(Gdk.PRIORITY_DEFAULT_IDLE, self.update_clocks)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
