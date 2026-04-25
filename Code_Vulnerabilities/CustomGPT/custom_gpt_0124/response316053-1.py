
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from time import gmtime, strftime
import threading

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start a thread to update the clock
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            GLib.idle_add(self.update)  # Schedule the update to run in the GTK main loop
            time.sleep(1)  # Update every second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and pack the Clock widget
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())

    def on_destroy(self, widget):
        Gtk.main_quit()

win = MainWindow()
win.connect("destroy", win.on_destroy)
win.show_all()
Gtk.main()
