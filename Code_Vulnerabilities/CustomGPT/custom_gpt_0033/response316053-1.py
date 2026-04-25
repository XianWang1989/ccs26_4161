
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
        self.update_timer()

    def update_timer(self):
        # Update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        return True  # Continue calling this function

    def widget(self):
        return self.gtkwidget

class MyApp:
    def __init__(self):
        self.window = Gtk.Window(title="Clock Example")
        self.window.set_default_size(300, 100)

        # Create Clock widgets
        self.clock1 = Clock(self.window, "Clock1")
        self.clock2 = Clock(self.window, "Clock2", format="%H:%M")

        # Layout
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(self.clock1.widget(), True, True, 0)
        box.pack_start(self.clock2.widget(), True, True, 0)

        self.window.add(box)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

if __name__ == "__main__":
    MyApp()
    Gtk.main()
