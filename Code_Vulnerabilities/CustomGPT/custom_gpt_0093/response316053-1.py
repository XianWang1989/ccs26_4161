
import gi
import time
from gi.repository import Gtk, GLib

class ClockWidget:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name(name)

        # Start the update loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = time.strftime(self.format, time.gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout active

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        clock1 = ClockWidget(self, "Clock1")
        self.add(clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
