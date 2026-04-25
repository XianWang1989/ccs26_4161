
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent_name, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name + parent_name
        self.gtkwidget.set_name(self.name)

        # Schedule the update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout active

    def widget(self):
        return self.gtkwidget

class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        self.clock = Clock("Window", "Clock1")
        self.add(self.clock.widget())
        self.connect("destroy", Gtk.main_quit)

window = ParentWindow()
window.show_all()
Gtk.main()
