
from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)

    def update(self):
        time_text = strftime(self.format, gmtime())
        self.gtkwidget.set_text(time_text)
        self.gtkwidget.queue_draw()  # Ensure redraw

    def widget(self):
        return self.gtkwidget
