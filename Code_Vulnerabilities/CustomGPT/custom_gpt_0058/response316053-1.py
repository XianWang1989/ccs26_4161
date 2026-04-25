
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class WidgetManager:
    def __init__(self):
        self.clock = Clock(window=self)  # Assuming you're passing the parent
        GLib.timeout_add(1000, self.update_clocks)  # Call update every second

    def update_clocks(self):
        self.clock.update()
        return True  # Keep the timeout running

# Within your Clock class, update the definition
def update(self):
    current_time = strftime(self.format, gmtime())
    print("Setting clock text to", current_time)
    self.gtkwidget.set_text(current_time)
    self.gtkwidget.queue_draw()  # Request a redraw, although it may not be necessary

