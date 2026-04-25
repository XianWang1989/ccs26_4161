
from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.update_clock()  # Initial update
        GLib.timeout_add_seconds(1, self.update)  # Schedule updates

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout active

    def get_widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.get_widget())
        self.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
