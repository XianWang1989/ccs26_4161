
#!/usr/bin/env python

from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class ClockWidget:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensure it redraws if needed

    def get_widget(self):
        return self.gtkwidget

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = ClockWidget(self, "Clock1")
        self.clock2 = ClockWidget(self, "Clock2", format="%H:%M")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.pack_start(self.clock1.get_widget(), True, True, 0)
        self.box.pack_start(self.clock2.get_widget(), True, True, 0)

        self.add(self.box)

        # Start the update loop
        GLib.timeout_add_seconds(1, self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        self.clock2.update()
        return True  # Return True to continue calling this function

if __name__ == "__main__":
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
