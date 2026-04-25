
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, parent, name, format="%H:%M:%S"):
        super().__init__()
        self.parent = parent
        self.format = format
        self.set_name(name)
        self.set_text(strftime(self.format, gmtime()))

    def update(self):
        new_time = strftime(self.format, gmtime())
        self.set_text(new_time)
        self.parent.refresh_label(self)

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2", format="%H:%M")

        self.grid.attach(self.clock1, 0, 0, 1, 1)
        self.grid.attach(self.clock2, 0, 1, 1, 1)

        self.show_all()

    def refresh_label(self, clock_widget):
        # This function can be used to perform any additional operations
        print(f"Updated label: {clock_widget.get_text()}")

def main():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)

    # Simulating the timer to update clocks every second
    def update_clocks():
        win.clock1.update()
        win.clock2.update()
        return True

    Gtk.timeout_add(1000, update_clocks)
    Gtk.main()

if __name__ == "__main__":
    main()
