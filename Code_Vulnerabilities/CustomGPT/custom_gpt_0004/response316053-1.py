
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock(Gtk.Label):
    def __init__(self, format="%H:%M:%S"):
        super().__init__()
        self.format = format
        self.set_gtk_label()
        # Set up a timeout to update the clock
        Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT, self.update)

    def set_gtk_label(self):
        self.set_text(strftime(self.format, gmtime()))

    def update(self):
        self.set_text(strftime(self.format, gmtime()))
        # Schedule the next update in 1 second
        Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT, self.update)
        return False  # Return False to stop the timeout

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.clock1 = Clock(format="%H:%M:%S")
        self.clock2 = Clock(format="%H:%M")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(self.clock1, True, True, 0)
        vbox.pack_start(self.clock2, True, True, 0)

        self.add(vbox)
        self.show_all()

# Main execution
if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
