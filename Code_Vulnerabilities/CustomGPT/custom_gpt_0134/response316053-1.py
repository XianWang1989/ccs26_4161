
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class ClockWidget:
    def __init__(self, parent):
        self.format = "%H:%M:%S"
        self.label = Gtk.Label()
        self.label.set_name("clock_label")
        parent.add(self.label)

        # Start the update timer
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        self.label.queue_draw()  # Force redraw
        return True  # Keep the timeout running

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock = ClockWidget(self)  # Pass self to ClockWidget

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
