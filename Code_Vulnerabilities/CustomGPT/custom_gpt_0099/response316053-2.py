
class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock App")
        self.clock_widget = Clock(self, "Clock1")
        self.timeout_id = Gdk.timeout_add(1000, self.update_clock)

    def update_clock(self):
        self.clock_widget.update()
        return True  # Continue timeout

win = ParentWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
