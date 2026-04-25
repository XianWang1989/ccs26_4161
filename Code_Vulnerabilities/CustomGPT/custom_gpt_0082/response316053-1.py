
#!/usr/bin/env python

from gi.repository import Gtk, GLib
import Defaults.widget

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget.set_name(name)

        # Start the timer to update the clock
        GLib.timeout_add(1000, self.update)  # Update every 1000 ms

    def update(self):
        new_time = strftime(self.format, gmtime())
        print("Setting clock text to", new_time)
        self.gtkwidget.set_text(new_time)
        self.gtkwidget.queue_draw()  # Ensure the widget is redrawn
        return True  # Keep the timeout active

    def get_widget(self):
        return self.gtkwidget
