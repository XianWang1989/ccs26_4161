
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.update()  # Initial call to set the clock text
        GLib.timeout_add(1000, self.update)  # Call update every second

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        return True  # Return True to continue calling this function

    def widget(self):
        return self.gtkwidget

# Example parent class to showcase usage

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())
        self.connect("destroy", Gtk.main_quit)

# Main execution
if __name__ == "__main__":
    win = MainWindow()
    win.show_all()
    Gtk.main()
