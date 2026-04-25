
class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)  # Assuming you're adding it to the parent

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force a redraw
        # Alternative method to find widget by name
        labeled_widget = self.parent.get_child_by_name(self.name)
        if labeled_widget:
            labeled_widget.set_text(current_time)
            labeled_widget.queue_draw()

# Usage example:
# Assuming `main_window` is your Gtk.Window
my_clock = Clock(main_window, "Clock1")
