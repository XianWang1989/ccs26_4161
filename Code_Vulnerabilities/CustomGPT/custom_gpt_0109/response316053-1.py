
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent
        self.is_running = True

        # Schedule the update to run every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        if not self.is_running:
            return False  # Stop the timer if not running

        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timer running

    def stop(self):
        self.is_running = False  # Method to stop the update

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock_widget = Clock(self, "clock_label")

        # Adding the clock widget to the window
        self.add(self.clock_widget.widget())
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
