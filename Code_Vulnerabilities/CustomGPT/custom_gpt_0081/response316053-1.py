
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime
import Defaults.widget  # Ensure you have a default format defined

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = Defaults.widget.defaultClockFormat
        self.name = name

        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)

        self.update_id = GLib.timeout_add(1000, self.update)  # Call `update` every 1 second

    def update(self):
        # Update the label's text and ensure it's called on the main thread
        current_time = strftime(self.format, gmtime())
        GLib.idle_add(self.gtkwidget.set_text, current_time)
        return True  # Keep the timeout active

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1]
            else:
                print(f"{configurationFile}, line {lineCount}: Badly formatted command 'format'. Skipping...")

    def widget(self):
        return self.gtkwidget

# Example usage of the Clock class in a Gtk.Window subclass
class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Clock Example")

        self.set_default_size(200, 100)

        # Create a box to pack widgets
        box = Gtk.Box()
        self.add(box)

        # Instantiate the Clock widget
        self.clock = Clock(self, "myClock")
        box.pack_start(self.clock.widget(), True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
