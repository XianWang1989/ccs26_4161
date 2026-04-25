
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading
import gi

gi.require_version("Gtk", "3.0")

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start a thread to update the clock every second
        threading.Thread(target=self.update_time, daemon=True).start()

    def update_time(self):
        while True:
            self.parent.update_clock(self.gtkwidget, strftime(self.format, gmtime()))
            time.sleep(1)

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

    def update_clock(self, child_widget, new_time):
        if child_widget.get_name() == self.clock1.name:
            child_widget.set_text(new_time)
            child_widget.queue_draw()  # Force a redraw

    def on_destroy(self, widget):
        Gtk.main_quit()

win = MainWindow()
win.connect("destroy", win.on_destroy)
win.show_all()
Gtk.main()
