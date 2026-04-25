
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading
import gi

gi.require_version("Gtk", "3.0")

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.format = format
        self.label = Gtk.Label()
        self.label.set_name(name)
        self.update_clock()

        # Start a thread to update the clock every second
        threading.Thread(target=self.run_update_thread, daemon=True).start()

    def run_update_thread(self):
        while True:
            self.update_clock()
            time.sleep(1)  # Update every second

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        Gtk.idle_add(self.label.set_text, current_time)  # Update the label safely

    def widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create clock instances
        self.clock1 = Clock(self, "Clock1", format="%H:%M:%S")
        self.clock2 = Clock(self, "Clock2", format="%H:%M")

        # Pack widgets into the window
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(self.clock1.widget(), True, True, 0)
        box.pack_start(self.clock2.widget(), True, True, 0)

        self.add(box)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
