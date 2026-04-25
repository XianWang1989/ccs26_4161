
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget.set_name(name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.parent.update_child_text(self.gtkwidget, current_time)
        self.gtkwidget.queue_draw()  # Ensure visibility update

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_size_request(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        self.show_all()

    def update_child_text(self, child, text_to_set):
        if child == self.clock1.widget():
            self.clock1.widget().set_text(text_to_set)
            self.clock1.widget().queue_draw()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
