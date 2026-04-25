
from gi.repository import Gtk, GLib
from time import gmtime, strftime

class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.gtkwidget.set_name(name)

        # Update the clock every second
        GLib.timeout_add(1000, self.update)

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.gtkwidget.set_text(current_time)
        self.parent.runFromChildToParent(self.gtkwidget, current_time)
        return True  # Return True to continue the timeout

    def runCommand(self, command):
        if command.startswith("format="):
            self.format = command.split("=")[1]

    def widget(self):
        return self.gtkwidget


class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")
        self.set_default_size(300, 200)
        self.clock = Clock(self, "ClockLabel")
        self.add(self.clock.widget())

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def runFromChildToParent(self, child, textToSet):
        # Access children to confirm updates
        for child_widget in self.get_children():
            if isinstance(child_widget, Gtk.Label) and child_widget.get_name() == child.get_name():
                child_widget.set_text(textToSet)
                break


if __name__ == "__main__":
    win = ParentWindow()
    Gtk.main()
