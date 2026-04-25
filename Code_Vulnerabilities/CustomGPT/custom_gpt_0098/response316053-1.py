
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)  # Add to parent

        self.update_time()  # Initial call to update time

    def update_time(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw
        GLib.timeout_add_seconds(1, self.update_time)  # Update every second

# Parent Window Example
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        self.connect("destroy", Gtk.main_quit)
        self.show_all()  # Show the window and its contents

# Main Application
if __name__ == "__main__":
    win = MyWindow()
    Gtk.main()
