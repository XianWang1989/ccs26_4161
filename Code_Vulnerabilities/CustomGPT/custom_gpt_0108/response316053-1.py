
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)

        # Start a thread to update the clock
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            self.update()
            Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT, self.parent.update_label, self.gtkwidget)
            time.sleep(1)

    def update(self):
        print("Updating clock text to", strftime(self.format, gmtime()))
        # Perform the update directly
        self.gtkwidget.set_text(strftime(self.format, gmtime()))

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        self.show_all()

    def update_label(self, clock_label):
        # Ensure the clock label updates properly
        clock_text = clock_label.get_text()
        print("Setting clock text to", clock_text)
        clock_label.queue_draw()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
