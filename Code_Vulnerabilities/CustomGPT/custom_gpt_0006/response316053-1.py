
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class Clock():
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.name = name
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.update_clock()

        # Start a thread to continuously update the clock
        threading.Thread(target=self.run_update_thread, daemon=True).start()

    def update_clock(self):
        self.gtkwidget.set_text(strftime(self.format, gmtime()))

    def run_update_thread(self):
        while True:
            self.update_clock()
            self.gtkwidget.queue_draw()  # Request a redraw
            # Sleep for 1 second
            time.sleep(1)

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        # Create a clock
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

win = MainWindow()
Gtk.main()
