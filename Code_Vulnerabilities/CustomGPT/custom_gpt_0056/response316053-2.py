
class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        # Create Clock instances
        clock1 = Clock(self, "Clock1")
        vbox.pack_start(clock1.widget(), True, True, 0)

        self.show_all()

if __name__ == "__main__":
    win = MainWindow()
    Gtk.main()
