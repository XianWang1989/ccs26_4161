
from gi.repository import GLib

# In your MainWindow constructor, set a timer
GLib.timeout_add_seconds(1, self.update_clocks)

def update_clocks(self):
    for clock in self.clocks:
        clock.update()  # Call each clock's update function
    return True  # Keep the timer running
