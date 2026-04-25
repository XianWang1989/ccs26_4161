
import gi
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name(name)
        self.parent = parent
        self.update_clock()  # Initial update
        GLib.timeout_add_seconds(1, self.update_clock)  # Schedule updates every second

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        # Create Clock widget
        clock = Clock(self, "Clock1")
        self.add(clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    gi.require_version("Gtk", "3.0")
    Gtk.init()
    window = MainWindow()
    Gtk.main()
