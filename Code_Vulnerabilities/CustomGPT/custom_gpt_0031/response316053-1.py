
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update()

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)

    def runCommand(self, command):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) == 2:
                self.format = parts[1]

    def widget(self):
        return self.gtkwidget


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        # Create and add Clock widget
        clock1 = Clock(self, "Clock1")
        self.add(clock1.widget())

        self.show_all()

    def update_clock(self):
        # Call update on each Clock widget
        for child in self.get_children():
            if isinstance(child, Gtk.Label):
                child.set_text(strftime("%H:%M:%S", gmtime()))


def main():
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)

    # Update every second
    Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT_IDLE, win.update_clock)
    Gtk.main()

if __name__ == "__main__":
    main()
