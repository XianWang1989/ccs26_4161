
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class Clock():
    def __init__(self, parent, name):
        self.parent = parent  # Reference to the parent
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(name)  # Set name for identification
        self.format = "%H:%M:%S"

        self.update_clock()  # Start clock updates in a separate thread

    def update_clock(self):
        # Update the clock every second using a separate thread
        threading.Timer(1, self.update_clock).start()
        self.update()

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.parent.update_widget(self.name, current_time)  # Notify the parent

    def widget(self):
        return self.gtkwidget


class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_size_request(200, 200)
        self.connect("destroy", Gtk.main_quit)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.show_all()

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
    window = ParentWindow()
    Gtk.main()
