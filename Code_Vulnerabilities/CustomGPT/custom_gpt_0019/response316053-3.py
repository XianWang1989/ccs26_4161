
def start_update(self):
    self.clock1.update()  # Update each clock as needed
    # Schedule the next update
    GLib.timeout_add_seconds(1, self.start_update)
