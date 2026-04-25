
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent_name, name):
        self.format = "%H:%M:%S"  # default format
        self.gtkwidget = Gtk.Label()
        self.name = name + parent_name
        self.gtkwidget.set_name(self.name)

        # Schedule the update function to be called every 1 second
        GLib.timeout_add(1000, self.update)

    def update(self):
        text = strftime(self.format, gmtime())
        print("Setting clock text to", text)
        self.gtkwidget.set_text(text)
        return True  # Returning True keeps the timeout running

    def widget(self):
        return self.gtkwidget

# Example parent class
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        clock1 = Clock("1", "Clock")
        hbox.pack_start(clock1.widget(), True, True, 0)

        # Show all widgets
        self.show_all()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
