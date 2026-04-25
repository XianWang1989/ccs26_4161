
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, format="%H:%M:%S"):
        super().__init__()
        self.format = format
        self.set_name("ClockLabel")

        # Start the update loop
        self.update_clock()

    def update_clock(self):
        current_time = strftime(self.format, gmtime())
        self.set_text(current_time)

        # Use GLib to call this function every second
        GLib.timeout_add_seconds(1, self.update_clock)  # Schedule for every second

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(250, 100)

        # Create a clock widget
        self.clock = Clock()
        self.add(self.clock)

        # Connect the close event
        self.connect("destroy", Gtk.main_quit)

# Create and run the application
win = MainWindow()
win.show_all()
Gtk.main()
