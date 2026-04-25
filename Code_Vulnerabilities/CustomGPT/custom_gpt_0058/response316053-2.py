
class ParentWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.label = Gtk.Label(label="00:00:00")
        self.add(self.label)
        self.show_all()

    def update_label(self, text):
        self.label.set_text(text)
        self.label.queue_draw()  # Request a redraw  
