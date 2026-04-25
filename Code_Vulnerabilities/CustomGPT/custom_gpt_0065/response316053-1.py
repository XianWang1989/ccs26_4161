
#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from time import gmtime, strftime
import Defaults.widget  # Assuming this contains default format

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name
        self.gtkwidget.set_name(self.name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.parent.update_child_label(self.name, current_time)

    def runCommand(self, command, lineCount, configurationFile):
        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                print(f"{configurationFile}, line {lineCount}: Badly formatted command 'format'.")
                return
            self.format = parts[1]

    def widget(self):
        return self.gtkwidget

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())
        self.show_all()

    def update_child_label(self, name, text):
        widget = self.get_child_by_name(name)
        if widget:
            widget.set_text(text)

    def get_child_by_name(self, name):
        for child in self.get_children():
            if child.get_name() == name:
                return child
        return None

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
