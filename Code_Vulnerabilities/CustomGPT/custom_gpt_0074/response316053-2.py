
def update(self):
    current_time = strftime(self.format, gmtime())
    print("Updating label to:", current_time)  # Debug log
    self.gtkwidget.set_text(current_time)
    self.gtkwidget.queue_draw()  # Force redraw if needed
    return True
