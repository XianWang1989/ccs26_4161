
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import gi
import threading

class Clock():
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent = parent

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.parent.update_label(self.name, current_time)

    def start_updater(self):
        def update_thread():
            while True:
                self.update()
                # Update every second
                time.sleep(1)
        threading.Thread(target=update_thread, daemon=True).start()

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 200)

        self.clock1 = Clock(self, "Clock1")
        self.clock1.start_updater()
        self.add(self.clock1.gtkwidget)

    def update_label(self, name, text):
        child = self.get_children()[0]
        if child.get_name() == name:
            child.set_text(text)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
