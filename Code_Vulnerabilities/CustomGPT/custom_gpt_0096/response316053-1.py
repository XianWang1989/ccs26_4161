
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        # Initialize the label content
        self.update_label()

        # Set up a timeout to update the label every second
        GLib.timeout_add(1000, self.update_label)

    def update_label(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout running

    def get_widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        # Create clock instance
        clock1 = Clock(self, "Clock1")
        vbox.pack_start(clock1.get_widget(), True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

win = MainWindow()
Gtk.main()
