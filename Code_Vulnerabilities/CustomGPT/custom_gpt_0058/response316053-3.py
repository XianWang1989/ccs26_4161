
def update(self):
    current_time = strftime(self.format, gmtime())
    print("Setting clock text to", current_time)
    self.parent.update_label(current_time)  # Update the parent label directly
