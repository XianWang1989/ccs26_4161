
from gi.repository import Gtk, Gdk
from time import gmtime, strftime
from threading import Timer

class Clock:
    def __init__(self, parent, name, format="%H:%M:%S"):
        self.parent = parent
        self.name = name
        self.format = format
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.update_label()  # Initial update
        self.parent.add(self.gtkwidget)  # Add the clock label to the parent

    def update_label(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw
        Timer(1, self.update_label).start()  # Schedule next update

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock widgets
        self.clock1 = Clock(self, "Clock1", "%H:%M:%S")
        self.clock2 = Clock(self, "Clock2", "%H:%M")

        self.show_all()  # Show all widgets

# Start the application
if __name__ == "__main__":
    Gtk.init([])
    win = MainWindow()
    Gtk.main()
