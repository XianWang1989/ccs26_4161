
from gi.repository import Gtk
import time

class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")

        self.set_default_size(200, 100)
        self.label = Gtk.Label()
        self.label.set_name("ClockLabel")  # Set the name for access
        self.add(self.label)

        self.clock = Clock(self, "ClockLabel", "%H:%M:%S")

        # Set up a timer to update the clock
        GLib.timeout_add(1000, self.update_clock)

    def update_clock(self):
        self.clock.update()
        return True  # Continue the timeout

    def runFromChildToParent(self, text_to_set):
        # Find child by name and update it
        child = self.get_child_by_name("ClockLabel")
        if child:
            child.set_text(text_to_set)
            child.queue_draw()  # Ensure it redraws

    def get_child_by_name(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None
