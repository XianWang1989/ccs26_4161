
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, format="%H:%M:%S"):
        self.format = format
        self.gtkwidget = Gtk.Label()
        GLib.timeout_add(1000, self.update)  # Call update every 1000ms

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # return True to continue the timeout

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock App")
        self.set_default_size(200, 100)

        # Create Clock instances
        clock1 = Clock(format="%H:%M:%S")
        clock2 = Clock(format="%H:%M")

        # Add clocks to the window
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(clock1.widget(), True, True, 0)
        box.pack_start(clock2.widget(), True, True, 0)

        self.add(box)
        self.connect("destroy", Gtk.main_quit)

win = MainWindow()
win.show_all()
Gtk.main()
