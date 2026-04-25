
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Example default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)  # Add directly to parent

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensure it gets redrawn

class WidgetManager:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.connect("destroy", Gtk.main_quit)
        self.clock_widget = Clock(self.window, "Clock1")
        self.window.show_all()
        self.update_clock()

    def update_clock(self):
        self.clock_widget.update()
        Gdk.threads_add_idle(Gdk.PRIORITY_DEFAULT_IDLE, self.update_clock)

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    manager = WidgetManager()
    manager.run()
