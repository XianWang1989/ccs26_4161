
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.update()  # Initialize with the current time

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.parent.runFromChildToParent(self.gtkwidget, current_time)

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=", 1)[1].strip()

    def widget(self):
        return self.gtkwidget

# Parent Window Class
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_size_request(300, 200)

        # Create Clock instances
        self.clocks = []
        self.clocks.append(Clock(self, "Clock1"))
        self.clocks.append(Clock(self, "Clock2"))

        # Adding the widgets to the window
        for clock in self.clocks:
            self.add(clock.widget())

        self.show_all()
        self.update_clocks()

    def runFromChildToParent(self, child_widget, text_to_set):
        # Ensure only updating the correct child
        for child in self.get_children():
            if child.get_name() == child_widget.get_name():
                child.set_text(text_to_set)
                break

    def update_clocks(self):
        for clock in self.clocks:
            clock.update()
        # Schedule the next update
        Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT, self.update_clocks)

# Main loop
if __name__ == "__main__":
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
