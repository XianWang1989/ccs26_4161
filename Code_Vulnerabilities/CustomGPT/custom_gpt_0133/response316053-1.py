
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class ClockWidget:
    def __init__(self, parent):
        self.gtkwidget = Gtk.Label()
        self.parent = parent
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name("ClockLabel")

        # Schedule update every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True to continue calling this function

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock_widget = ClockWidget(self)
        self.add(self.clock_widget.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == '__main__':
    win = MainWindow()
    Gtk.main()
