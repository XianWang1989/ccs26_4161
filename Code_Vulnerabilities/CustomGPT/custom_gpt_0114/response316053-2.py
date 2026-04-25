
class MyApp(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        self.clock1 = Clock(self, "Clock1")
        self.add(self.clock1.widget())

        # Setup an update timer
        GLib.timeout_add(1000, self.update_clocks)

    def update_clocks(self):
        self.clock1.update()
        return True  # Continue this timer

# Entry point
if __name__ == "__main__":
    app = MyApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
