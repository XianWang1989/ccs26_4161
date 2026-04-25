
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        # Store a reference to the parent
        self.parent = parent

        # Set up a GLib timeout to update every second
        GLib.timeout_add_seconds(1, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw
        return True  # Keep the timeout active

    def get_widget(self):
        return self.gtkwidget

# Example usage in a parent widget
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        clock = Clock(self, "Clock1")
        self.add(clock.get_widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Run the GTK application
if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
