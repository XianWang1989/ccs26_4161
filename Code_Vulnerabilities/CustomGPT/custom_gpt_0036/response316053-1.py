
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime
import threading
import sys

class Clock(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.label = Gtk.Label()
        self.label.set_name("clock_label")
        self.add(self.label)

        # Start the clock update thread
        self.update_thread = threading.Thread(target=self.update_clock)
        self.update_thread.daemon = True
        self.update_thread.start()

        self.connect("destroy", Gtk.main_quit)

    def update_clock(self):
        while True:
            # Updating the label text in a safe way
            GLib.idle_add(self.update_label, strftime("%H:%M:%S", gmtime()))
            # Sleep for one second
            time.sleep(1)

    def update_label(self, time_str):
        # This is called in the main thread
        self.label.set_text(time_str)

if __name__ == "__main__":
    win = Clock()
    win.show_all()
    Gtk.main()
