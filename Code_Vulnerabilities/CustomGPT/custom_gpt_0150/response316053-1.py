
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class Clock(Gtk.Label):
    def __init__(self, format="%H:%M:%S"):
        super().__init__()
        self.format = format
        self.set_name("ClockLabel")
        self.update_clock()

    def update_clock(self):
        self.set_text(strftime(self.format, gmtime()))
        self.queue_draw()
        # Schedule the next update
        threading.Timer(1, self.update_clock).start()

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock = Clock()
        self.add(self.clock)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
