
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format='%H:%M:%S'):
        self.parent = parent
        self.format = format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.parent.add(self.gtkwidget)  # Add label to parent
        self.update()  # Initial update
        GLib.timeout_add(1000, self.update)  # Update every second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw
        return True  # Return True to continue the timeout

    def set_format(self, new_format):
        self.format = new_format

# Example Gtk.Window subclass
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_size_request(300, 200)

        clock1 = Clock(self, "Clock1", "%H:%M:%S")
        clock2 = Clock(self, "Clock2", "%H:%M")

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
