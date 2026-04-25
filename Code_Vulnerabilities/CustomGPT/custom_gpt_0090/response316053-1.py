
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading
import time

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.label = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.label.set_name(name)
        self.update()  # Initial update

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        self.parent.runFromChildToParent(self.label, current_time)

    def widget(self):
        return self.label

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gtk Clock Example")
        self.set_size_request(200, 100)

        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())

        self.show_all()
        # Update every second
        threading.Thread(target=self.update_clock, daemon=True).start()

    def runFromChildToParent(self, child, textToSet):
        # Update child label text if it matches
        if child.get_name() == "Clock1":
            child.set_text(textToSet)
            child.queue_draw()

    def update_clock(self):
        while True:
            time.sleep(1)
            self.clock.update()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
