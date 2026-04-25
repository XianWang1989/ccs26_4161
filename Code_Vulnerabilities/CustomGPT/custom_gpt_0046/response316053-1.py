
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import threading

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 200)
        self.widget_dict = {}

        # Create Clock widgets from config
        self.create_clock("Clock1", "%H:%M:%S", "#FF0000")
        self.create_clock("Clock2", "%H:%M", "#00FF00")

        # Start update thread
        threading.Thread(target=self.update_clocks, daemon=True).start()

    def create_clock(self, name, time_format, color):
        clock = Clock(self, name, time_format, color)
        self.widget_dict[name] = clock.label
        self.add(clock.label)

    def update_clocks(self):
        while True:
            for clock in self.widget_dict.values():
                clock.queue_draw()  # Request a redraw
            time.sleep(1)  # Update every second

class Clock:
    def __init__(self, parent, name, time_format, color):
        self.parent = parent
        self.label = Gtk.Label()
        self.label.set_name(name)
        self.label.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(float(int(color[1:3], 16)) / 255.0,
                                                                          float(int(color[3:5], 16)) / 255.0,
                                                                          float(int(color[5:7], 16)) / 255.0,
                                                                          1.0))
        self.format = time_format
        self.update()

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.label.set_text(current_time)
        self.label.queue_draw()

if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
