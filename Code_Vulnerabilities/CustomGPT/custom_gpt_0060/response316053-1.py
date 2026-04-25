
from gi.repository import GLib

# Call update every second
GLib.timeout_add_seconds(1, self.update)  # This should be in your main window class
