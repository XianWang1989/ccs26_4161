
class MainApplication(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.clocks = []
        self.add_clocks_from_config()

    def add_clocks_from_config(self):
        # Suppose you read from a config to add clocks
        self.clocks.append(Clock(self, "Clock1", "%H:%M:%S"))
        self.grid = Gtk.Grid()
        for clock in self.clocks:
            self.grid.attach(clock.get_widget(), 0, 0, 1, 1)
        self.add(self.grid)
        self.show_all()
