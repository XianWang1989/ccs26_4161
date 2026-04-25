
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Set up the timer for updates
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        if self.gtkwidget.get_text() != current_time:
            print("Updating clock to", current_time)
            self.gtkwidget.set_text(current_time)
            self.gtkwidget.queue_draw()  # Request redraw
        return True  # Return True to continue the timeout

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instance
        self.clock = Clock(self, "ClockWidget")
        self.add(self.clock.widget())

        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
