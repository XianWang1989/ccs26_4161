
#!/usr/bin/env python

from gi.repository import Gtk, GLib
from datetime import datetime

class Clock:
    def __init__(self, parent, name, format_='%H:%M:%S'):
        self.parent = parent
        self.name = name
        self.format = format_

        # Create a GTK Label and set its name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)
        self.parent.add(self.gtkwidget)

        # Schedule the update every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        # Update the label with the current time
        current_time = datetime.utcnow().strftime(self.format)
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensure it redraws
        return True  # Continue calling this function

    def get_widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create a Clock instance
        self.clock = Clock(self, "Clock1")

        self.show_all()

# Main Application
if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
