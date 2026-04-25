
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create the label that will display the time
        self.label = Gtk.Label()
        self.add(self.label)

        # Start updating the time every second
        GLib.timeout_add(1000, self.update_time)

    def update_time(self):
        # Get the updated time and set it to the label
        current_time = strftime("%H:%M:%S", gmtime())
        self.label.set_text(current_time)
        return True  # Keep the timeout active

# Run the application
win = Clock()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
