
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(name)  # Set the name to access it later

    def update(self):
        time_str = strftime(self.format, gmtime())
        self.gtkwidget.set_text(time_str)

        # Update the parent's label directly
        label = self.parent.get_widget_by_name(self.name)
        if label:
            label.set_text(time_str)
            label.queue_draw()  # Request a redraw if necessary

    def runCommand(self, command):
        if command.startswith("format="):
            _, new_format = command.split("=")
            self.format = new_format.strip()

    def widget(self):
        return self.gtkwidget


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="GTK Clock Example")
        self.set_size_request(200, 200)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        # Set a timer to update the clock every second
        GLib.timeout_add_seconds(1, self.clock1.update)

        self.show_all()

    def get_widget_by_name(self, name):
        # Search for the widget by its name
        return self.get_child_by_name(name)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
