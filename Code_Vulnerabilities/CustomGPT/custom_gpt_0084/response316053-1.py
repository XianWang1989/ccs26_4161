
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class Clock(Gtk.Window):
    def __init__(self, clock_name, clock_format):
        super().__init__(title=clock_name)
        self.set_default_size(200, 100)

        self.label = Gtk.Label()
        self.label.set_name(clock_name)
        self.add(self.label)

        self.format = clock_format

        # Start the update thread
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            self.label.set_text(strftime(self.format, gmtime()))
            Gtk.main_iteration_do(False)
            time.sleep(1)  # Sleep for 1 second

if __name__ == "__main__":
    # Load from configuration (static for demonstration)
    clocks = {
        "Clock1": "%H:%M:%S",
        "Clock2": "%H:%M"
    }

    for name, format in clocks.items():
        Clock(name, format)

    Gtk.main()
