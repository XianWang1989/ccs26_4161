import threading
from gi.repository import Gtk, GLib
from time import strftime, gmtime, sleep

class ClockWidget(Gtk.Label):
    def __init__(self, time_format="%H:%M:%S"):
        super().__init__()
        self.time_format = time_format
        self.start_thread()

    def start_thread(self):
        thread = threading.Thread(target=self.update_time)
        thread.daemon = True
        thread.start()

    def update_time(self):
        while True:
            current_time = strftime(self.time_format, gmtime())
            GLib.idle_add(self.set_text, current_time)
            sleep(1)

# Example usage
win = Gtk.Window(title="Clock Example")
clock = ClockWidget()
win.add(clock)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
