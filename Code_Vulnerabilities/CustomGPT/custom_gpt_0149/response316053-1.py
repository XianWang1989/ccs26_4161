
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Set default format
        self.name = name
        self.gtkwidget.set_name(self.name)

    def update(self):
        time_text = strftime(self.format, gmtime())
        self.gtkwidget.set_text(time_text)
        self.parent.update_child_text(self.name, time_text)  # Update parent widget text

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.clock = Clock(self, "Clock1")
        self.add(self.clock.widget())
        self.show_all()

    def update_child_text(self, widget_name, text):
        widget = self.get_child_by_name(widget_name)
        if widget:
            widget.set_text(text)
            widget.queue_draw()  # Force redraw

    def get_child_by_name(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
