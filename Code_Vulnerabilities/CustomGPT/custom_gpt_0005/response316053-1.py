
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, name, format="%H:%M:%S"):
        self.gtkwidget = Gtk.Label()
        self.format = format
        self.name = name
        self.gtkwidget.set_name(name)
        self.update()  # Initial call to set time

        # Setup a GLib timeout to periodically update the clock
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Continue the timeout

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock("Clock1", "%H:%M:%S")
        self.clock2 = Clock("Clock2", "%H:%M")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(self.clock1.widget(), True, True, 0)
        vbox.pack_start(self.clock2.widget(), True, True, 0)

        self.add(vbox)

    def run(self):
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()


if __name__ == "__main__":
    MainWindow().run()
