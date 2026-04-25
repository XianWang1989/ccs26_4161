
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update_clock()

    def update_clock(self):
        self.gtkwidget.set_text(strftime(self.format, gmtime()))
        self.gtkwidget.queue_draw()
        # Schedule next update
        Gdk.threads_add_idle(self.update_clock)

    def update_format(self, new_format):
        self.format = new_format

    def get_widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.pack_start(self.clock1.get_widget(), True, True, 0)
        self.box.pack_start(self.clock2.get_widget(), True, True, 0)

        self.add(self.box)
        self.connect("destroy", Gtk.main_quit)

        # Start clock updates in a separate thread
        threading.Thread(target=self.start_clock_updates, daemon=True).start()

    def start_clock_updates(self):
        while True:
            # Trigger Gtk main loop to keep UI responsive
            Gtk.main_iteration_do(False)


if __name__ == "__main__":
    window = MainWindow()
    window.show_all()
    Gtk.main()
