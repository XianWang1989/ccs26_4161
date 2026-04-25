
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start the update loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Continue calling this function

    def widget(self):
        return self.gtkwidget


class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")

        self.clock_widget = Clock(self, "Clock1")
        self.add(self.clock_widget.widget())
        self.show_all()


win = ParentWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
