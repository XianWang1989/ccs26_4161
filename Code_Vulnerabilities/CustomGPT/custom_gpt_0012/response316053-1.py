
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name("ClockLabel")
        self.update()
        GLib.timeout_add(1000, self.update)  # Call update every 1000ms (1 second)

    def update(self):
        time_text = strftime(self.format, gmtime())
        self.gtkwidget.set_text(time_text)
        return True  # Return True to continue calling this function

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock = Clock(self)
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
