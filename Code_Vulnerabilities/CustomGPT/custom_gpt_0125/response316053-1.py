
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import signal

class Clock(Gtk.Label):
    def __init__(self, format="%H:%M:%S", parent=None):
        super().__init__()
        self.format = format
        self.parent = parent
        self.set_name("clock_label")
        self.update_clock()

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        self.set_text(current_time)
        self.parent.queue_draw()  # Ensure the parent updates
        Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT_IDLE, self.update_clock)

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock = Clock(parent=self)
        self.add(self.clock)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Handle Ctrl+C
    window = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
