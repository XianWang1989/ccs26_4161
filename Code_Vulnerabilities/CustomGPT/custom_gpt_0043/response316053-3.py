
class WidgetManager:
    def create_clock(self, parent, name):
        clock_widget = Clock(parent, name)
        parent.add(clock_widget.widget())
        return clock_widget  # Keep a reference to it if needed

# Parent class managing children
class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        # other initializations
        self.manager = WidgetManager()
        self.clock1 = self.manager.create_clock(self, "Clock1")
        self.clock2 = self.manager.create_clock(self, "Clock2")
