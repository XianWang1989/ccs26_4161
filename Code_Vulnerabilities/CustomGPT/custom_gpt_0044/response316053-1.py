
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
import output, Defaults.widget
from time import gmtime, strftime
import threading

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget.set_name(self.name)

        # Start a thread to update the clock
        threading.Thread(target=self.update_clock, daemon=True).start()

    def update_clock(self):
        while True:
            self.update()
            # Sleep for one second before updating again
            time.sleep(1)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.parent.runFromChildToParent(self.gtkwidget, current_time)

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                output.stderr(f"{configurationFile}, line {lineCount}: Badly formatted command 'format'.\nSkipping...")
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Display")
        self.set_default_size(300, 200)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

    def runFromChildToParent(self, child, textToSet):
        if child.get_name() == self.clock1.gtkwidget.get_name():
            print("Updating label text")
            child.set_text(textToSet)

# Create and run the application
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
