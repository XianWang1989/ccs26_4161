
import GLib

class WidgetManager:
    def __init__(self):
        self.clocks = []  # Store clock instances

    def add_clock(self, name):
        clock = Clock(self, name)
        self.clocks.append(clock)
        # For demonstration, use a fixed position/layout
        self.get_main_window().add(clock.widget())
        clock.update()  # Initial update

    def start_clock_updates(self):
        for clock in self.clocks:
            GLib.timeout_add(1000, clock.update)  # Update every second

    def get_main_window(self):
        # Return your main window here
        pass
