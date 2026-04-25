
from gi.repository import Gtk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)  # Add to parent

    def update(self):
        text = strftime(self.format, gmtime())
        self.gtkwidget.set_text(text)
        self.gtkwidget.queue_draw()  # Request a redraw

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock = Clock(self, "ClockLabel")
        self.show_all()
        self.update_clock()

    def update_clock(self):
        self.clock.update()
        GLib.timeout_add_seconds(1, self.update_clock)  # Update every second

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
