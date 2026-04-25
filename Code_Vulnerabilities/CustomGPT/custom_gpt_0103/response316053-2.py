
class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # Create and add clocks
        clock1 = Clock(self.box, "Clock1")
        clock2 = Clock(self.box, "Clock2")

    def on_destroy(self, widget):
        Gtk.main_quit()

if __name__ == "__main__":
    window = MainWindow()
    window.connect("destroy", window.on_destroy)
    window.show_all()
    Gtk.main()
