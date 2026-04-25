
from gi.repository import Gtk, Gdk, GLib
from time import gmtime, strftime

class Clock():
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Initialize timer for updating clock every second
        GLib.timeout_add(1000, self.update)  # 1000 ms = 1 second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # to continue the timeout

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.set_default_size(300, 200)

        # Layout
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # Adding Clock widget
        self.clock1 = Clock(self, "Clock1")
        self.box.pack_start(self.clock1.widget(), True, True, 0)

        self.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
