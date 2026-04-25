
class MyMainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock Example")

        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        clock1 = Clock(self, "Clock1")
        clock2 = Clock(self, "Clock2")

        vbox.pack_start(clock1.widget(), True, True, 0)
        vbox.pack_start(clock2.widget(), True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

app = MyMainWindow()
Gtk.main()
