
def update(self):
    time_text = strftime(self.format, gmtime())
    widget_to_update = self.parent.get_children()  # Get children of the parent
    for child in widget_to_update:
        if child.get_name() == self.name:  # Match by name
            child.set_text(time_text)
            child.queue_draw()  # Force redraw
