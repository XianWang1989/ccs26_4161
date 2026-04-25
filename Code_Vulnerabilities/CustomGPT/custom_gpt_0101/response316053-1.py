
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

# Example Clock class
class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(name)
        self.parent.add(self.gtkwidget)

        # Start the update loop in a separate thread
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            self.update()
            Gtk.main_iteration_do(False)  # Force GUI update
            time.sleep(1)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw if necessary

# Example parent window
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_size_request(200, 100)
        self.connect("destroy", Gtk.main_quit)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        self.show_all()

# Main execution
if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
