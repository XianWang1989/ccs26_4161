
class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"
        self.gtkwidget.set_name("ClockLabel")

    def update(self):
        current_time = strftime(self.format, gmtime())
        self.parent.runFromChildToParent(self.gtkwidget, current_time)

class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.clock = Clock(self)
        self.add(self.clock.gtkwidget)

    def runFromChildToParent(self, child, textToSet):
        # Ensure the correct child is being updated
        if child.get_name() == "ClockLabel":
            child.set_text(textToSet)
            child.queue_draw()  # Force redraw
