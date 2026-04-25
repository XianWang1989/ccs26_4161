
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
        self.gtkwidget.set_name(name)

        # Start a thread to update the clock
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            self.update()
            time.sleep(1)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

        # Force redraw if needed
        self.gtkwidget.queue_draw()

    def get_widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_size_request(200, 100)

        # Initialize clock widgets
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        # Add widgets to the window
        self.add(self.clock1.get_widget())
        self.add(self.clock2.get_widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Run the application
if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
