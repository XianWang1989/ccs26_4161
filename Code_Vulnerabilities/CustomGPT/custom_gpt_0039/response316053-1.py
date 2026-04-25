
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start the update loop
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Keep the timeout active

    def widget(self):
        return self.gtkwidget

# Example usage of Clock in a Gtk.Window
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        clock_widget = Clock(self, "Clock1")
        self.add(clock_widget.widget())

        self.connect("destroy", Gtk.main_quit)

# Run the application
if __name__ == "__main__":
    win = MainWindow()
    win.show_all()
    Gtk.main()
