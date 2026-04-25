
class MethodTracker:
    def __init__(self):
        self.recent_methods = []

    def track_method(self, method_name):
        self.recent_methods.append(method_name)
        if len(self.recent_methods) > 5:  # Keep last 5 methods
            self.recent_methods.pop(0)

    def display_recent_methods(self):
        print("Recent methods called:", self.recent_methods)

# Example usage

tracker = MethodTracker()

def example_method_one():
    tracker.track_method('example_method_one')

def example_method_two():
    tracker.track_method('example_method_two')

example_method_one()
example_method_two()
tracker.display_recent_methods()
