
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent  # Store reference to parent if needed

    def update(self):
        # Update the label text
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensures widget is redrawn if necessary

    def get_widget(self):
        return self.gtkwidget

# Example Parent Class
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.get_widget())

        # Call update every second
        self.timeout_id = Gdk.threads_add_timeout_seconds(1, self.update_clock)

    def update_clock(self):
        self.clock.update()
        return True  # Keep the timeout active

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
