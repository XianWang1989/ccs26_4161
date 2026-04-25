
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading
import time

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start a separate thread to update the clock
        self.update_thread = threading.Thread(target=self.update)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update(self):
        while True:
            self.parent.runFromChildToParent(self.gtkwidget, strftime(self.format, gmtime()))
            time.sleep(1)  # Update every second

    def widget(self):
        return self.gtkwidget


class ParentWindow(Gtk.Window):
    def __init__(self):
        super(ParentWindow, self).__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

    def runFromChildToParent(self, child, textToSet):
        # Check if the widget name matches the child's name and update text
        if child.get_name() == self.clock1.gtkwidget.get_name():
            child.set_text(textToSet)


if __name__ == "__main__":
    win = ParentWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
