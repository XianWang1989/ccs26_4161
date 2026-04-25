
#!/usr/bin/env python

from gi.repository import Gtk
from time import gmtime, strftime
import threading

class WidgetManager:
    def __init__(self):
        self.widgets = {}
        self.window = Gtk.Window()
        self.window.set_title("Clock Application")
        self.window.set_size_request(400, 200)
        self.window.connect("destroy", Gtk.main_quit)

        self.start_clock_updater()

    def add_widget(self, widget):
        self.widgets[widget.name] = widget
        self.window.add(widget.widget())

    def start_clock_updater(self):
        # Update clocks every second
        threading.Thread(target=self.update_clocks, daemon=True).start()

    def update_clocks(self):
        while True:
            for widget in self.widgets.values():
                widget.update()
            time.sleep(1)

    def show(self):
        self.window.show_all()
        Gtk.main()

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.format = "%H:%M:%S"
        self.name = name
        self.gtkwidget = Gtk.Label()
        self.gtkwidget.set_name(self.name)
        self.update()  # Initialize once on creation

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw

    def widget(self):
        return self.gtkwidget

if __name__ == "__main__":
    manager = WidgetManager()
    manager.add_widget(Clock(manager, "Clock1"))
    manager.add_widget(Clock(manager, "Clock2"))
    manager.show()
