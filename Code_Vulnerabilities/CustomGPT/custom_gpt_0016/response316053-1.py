
#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.label = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.label.set_name("clock")  # Setting the name for later access
        self.update()  # Initial call to update the label

        # Using GLib.timeout_add to update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        return True  # Return True to continue the timeout

    def widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Adding the Clock widget
        clock = Clock(self)
        self.add(clock.widget())

# Run the application
if __name__ == '__main__':
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
