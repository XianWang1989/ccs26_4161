
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.format = "%H:%M:%S"  # Setting a default format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        # Start the updating loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Continue calling this function

    def widget(self):
        return self.gtkwidget

class MainApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.show_all()

if __name__ == "__main__":
    app = MainApp()
    Gtk.main()
