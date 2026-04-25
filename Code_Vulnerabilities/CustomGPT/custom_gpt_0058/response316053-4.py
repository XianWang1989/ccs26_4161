
class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.gtkwidget = Gtk.Label()
        self.update()  # Initial call to set the clock

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.parent.update_label(current_time)
        self.gtkwidget.queue_draw()  # Request a redraw

# Usage with WidgetManager
class WidgetManager:
    def __init__(self):
        self.clock = Clock(self)  # Pass parent to Clock
        GLib.timeout_add(1000, self.clock.update)  # Schedule update

# Run the Gtk main loop normally
win = ParentWindow()
manager = WidgetManager()
Gtk.main()
