
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 200)

        # Example of creating clocks
        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        # ... initialize other clocks as needed

    def runFromChildToParent(self, child, textToSet):
        for childd in self.get_children():
            if isinstance(childd, Gtk.Label) and childd.get_name() == child.get_name():
                childd.set_text(textToSet)
                break
