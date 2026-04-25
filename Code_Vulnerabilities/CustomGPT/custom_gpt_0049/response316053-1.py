
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock():
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Suggest a redraw
        return True  # Keep the timeout active

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

    def widget(self):
        return self.gtkwidget

# Example of how to create the Clock widget
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.clock1 = Clock(self, "Clock1")

        # Add the clock widget to the window
        self.add(self.clock1.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

# Run the GTK application
win = MyWindow()
Gtk.main()
