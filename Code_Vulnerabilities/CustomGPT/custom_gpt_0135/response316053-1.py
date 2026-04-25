
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import output, Defaults.widget

class Clock():
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget.set_name(self.name)
        self.parent.add(self.gtkwidget)  # Adding the label to the parent

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Force redraw to ensure display is updated

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                output.stderr(f"{configurationFile}, line {lineCount}: Badly formatted command 'format': Format: format = format.\nSkipping...")
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget

# Example parent window class
class MyApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(300, 200)
        self.clock1 = Clock(self, "Clock1")
        self.clock2 = Clock(self, "Clock2")

        Gtk.Timeout.add(1000, self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        self.clock2.update()
        return True  # Continue the timeout

win = MyApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
