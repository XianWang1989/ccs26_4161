
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)  # Set the name for later access
        self.parent = parent  # Store parent reference

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)

        # Access label by name (optional way)
        label = self.parent.get_widget_by_name(self.name)
        if label:
            label.set_text(current_time)
            label.queue_draw()  # Force a redraw

    def runCommand(self, command):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1]

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(300, 200)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(self.clock1.widget(), True, True, 0)
        vbox.pack_start(self.clock2.widget(), True, True, 0)
        self.add(vbox)

        self.show_all()

        # Simulate a timer for updating
        Gdk.threads_add_idle(self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        self.clock2.update()
        return True  # Repeat this call

    def get_widget_by_name(self, name):
        for child in self.get_children():
            widget = child.get_child_by_name(name)
            if widget:
                return widget
        return None


if __name__ == "__main__":
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()
