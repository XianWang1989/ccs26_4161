
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, clock_format="%H:%M:%S"):
        self.parent = parent
        self.format = clock_format
        self.gtkwidget = Gtk.Label()
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.gtkwidget.set_text(strftime(self.format, gmtime()))

        # Start the update loop
        GLib.timeout_add(1000, self.update)  # Update every 1000 ms (1 second)

    def update(self):
        new_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(new_time)
        self.gtkwidget.queue_draw()  # Ensure the widget is redrawn
        return True  # Continue calling this function

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock widgets
        clock1 = Clock(self, "Clock1")
        clock2 = Clock(self, "Clock2", "%H:%M")

        # Add widgets to the main window
        box = Gtk.Box()
        box.pack_start(clock1.widget(), True, True, 0)
        box.pack_start(clock2.widget(), True, True, 0)
        self.add(box)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
