
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime, sleep
import threading

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)

        # Start a separate thread to update the clock
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            text = strftime(self.format, gmtime())
            Gdk.threads_enter()  # Enter the GTK thread lock
            self.gtkwidget.set_text(text)
            Gdk.threads_leave()  # Leave the GTK thread lock
            sleep(1)  # Update every second

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.clocks = []

        # Create Clock widgets
        clock1 = Clock(self, "Clock1")
        self.add(clock1.widget())
        self.clocks.append(clock1)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Gtk.init()
    window = MainWindow()
    Gtk.main()
