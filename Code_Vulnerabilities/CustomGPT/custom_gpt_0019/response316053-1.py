
class Clock:
    def __init__(self, parent, name):
        self.parent = parent
        self.gtkwidget = Gtk.Label()
        self.format = "%H:%M:%S"  # Default format
        self.name = name
        self.gtkwidget.set_name(self.name)

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)
        # Directly set the text on self.gtkwidget
        self.gtkwidget.set_text(current_time)
        self.queue_redraw()

    def queue_redraw(self):
        self.gtkwidget.queue_draw()  # Request a redraw

    def widget(self):
        return self.gtkwidget
