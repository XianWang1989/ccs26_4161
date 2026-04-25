
def __init__(self, parent, name):
    self.parent = parent
    self.gtkwidget = Gtk.Label()
    self.format = Defaults.widget.defaultClockFormat
    self.name = name + parent.get_name()  # Use parent's name to formulate the name
    self.gtkwidget.set_name(self.name)

    # Start the update loop
    GLib.timeout_add_seconds(1, self.update)  # Call update every second
