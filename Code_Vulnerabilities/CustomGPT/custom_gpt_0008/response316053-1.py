
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import Defaults.widget

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.update()  # Initial update

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)

        # Access parent to update the current widget
        self.parent.update_widget(self.name, current_time)

    def get_widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.clocks = []

        # Example of adding clocks based on a configuration
        self.add_clock("Clock1")
        self.add_clock("Clock2")

        self.show_all()

    def add_clock(self, name):
        clock = Clock(self, name)
        self.add(clock.get_widget())
        self.clocks.append(clock)

    def update_widget(self, name, text):
        widget = self.get_child_by_name(name)
        if widget:
            widget.set_text(text)

    def get_child_by_name(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None

if __name__ == "__main__":
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()
