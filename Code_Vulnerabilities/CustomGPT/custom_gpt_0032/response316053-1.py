
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import GLib  # Import for timeout handling

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)
        self.start_update()

    def start_update(self):
        # Call update function every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        # Ensure the widget is redrawn
        self.gtkwidget.queue_draw()
        return True  # Keep the timeout active

    def set_format(self, new_format):
        self.format = new_format

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(300, 200)

        # Load configurations and create Clock widgets
        clock1 = Clock(self, "Clock1")
        clock2 = Clock(self, "Clock2")

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

win = MyWindow()
Gtk.main()
