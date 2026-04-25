
class Clock:
    def __init__(self, parent, name):
        self.parent = parent  # Store a reference to the parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

    def update(self):
        new_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(new_time)

        # Update the parent's child by name
        if self.parent.update_label_by_name(self.name, new_time):
            print("Label updated successfully.")
        else:
            print("Label update failed.")

# Parent class with method to update the clock label
class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.gtkwidget)

    def update_label_by_name(self, name, text):
        widget = self.get_child_by_name(name)
        if widget:
            widget.set_text(text)
            return True
        return False

    def get_child_by_name(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None
