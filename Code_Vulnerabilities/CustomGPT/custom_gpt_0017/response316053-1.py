
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import Defaults.widget
import output

class Clock():
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update_interval = 1000  # 1 second

        # Start updating the clock
        Gdk.threads_add_idle(self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        # Queue a call to update again after the interval
        Gdk.threads_add_timeout(self.update_interval, self.update)
        return False  # This makes sure we don't get stuck in recursive calls

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instances based on your config
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(self.clock1.widget(), True, True, 0)
        vbox.pack_start(self.clock2.widget(), True, True, 0)

        self.add(vbox)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Gdk.threads_init()
    window = MainWindow()
    Gtk.main()
