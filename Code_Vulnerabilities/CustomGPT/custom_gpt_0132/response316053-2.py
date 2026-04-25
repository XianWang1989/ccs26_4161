
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Clock Example")
        self.set_default_size(200, 100)

        # Create Clock instance
        clock = Clock(self, "Clock1")
        self.add(clock.widget())
        self.show_all()

app = Gtk.Application()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
