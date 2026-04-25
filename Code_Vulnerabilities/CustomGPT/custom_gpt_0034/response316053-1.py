
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force a redraw if necessary

    def widget(self):
        return self.gtkwidget

class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock widgets
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        # Add to the window
        self.add(self.clock1.widget())
        self.add(self.clock2.widget())

        # Set up update function
        self.show_all()

    def run_update_cycle(self):
        # Update each Clock widget every second
        GLib.timeout_add(1000, self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        self.clock2.update()

def main():
    win = ParentWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
