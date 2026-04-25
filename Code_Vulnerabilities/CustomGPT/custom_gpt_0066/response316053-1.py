
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime
import threading


class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start a timer to update the clock every second
        threading.Thread(target=self.start_timer, daemon=True).start()

    def start_timer(self):
        while True:
            GLib.idle_add(self.update)
            time.sleep(1)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
