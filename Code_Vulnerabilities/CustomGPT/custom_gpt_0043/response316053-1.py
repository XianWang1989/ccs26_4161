
from gi.repository import GLib

# Inside your update function
def update(self):
    GLib.idle_add(self.update_label)

def update_label(self):
    print("Setting clock text to", strftime(self.format, gmtime()))
    self.gtkwidget.set_text(strftime(self.format, gmtime()))
    return False  # Return False to indicate that the function should be removed from the queue
