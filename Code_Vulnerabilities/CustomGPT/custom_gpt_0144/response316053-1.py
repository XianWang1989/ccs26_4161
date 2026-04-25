from gi.repository import Gtk, GLib
from time import strftime, gmtime

class ClockWidget(Gtk.Label):
    def __init__(self, time_format="%H:%M:%S"):
        super().__init__()
        self.time_format = time_format
        self.update_time()
        # Schedule the update_time function to be called every 1000 milliseconds (1 second)
        GLib.timeout_add(1000, self.update_time)

    def update_time(self):
        current_time = strftime(self.time_format, gmtime())
        self.set_text(current_time)
        # Returning True ensures the function is called again after the interval
        return True

# Example usage
win = Gtk.Window(title="Clock Example")
clock = ClockWidget()
win.add(clock)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
