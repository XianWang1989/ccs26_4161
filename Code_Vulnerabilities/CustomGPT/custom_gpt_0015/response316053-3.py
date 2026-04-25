
def update(self):
    current_time = strftime(self.format, gmtime())
    print("Updating time to:", current_time)
    self.gtkwidget.set_text(current_time)
    self.gtkwidget.queue_draw()  # Ensure it's redrawn
