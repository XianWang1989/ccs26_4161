
class MethodTracker:
    def __init__(self):
        self.recent_methods = []

    def track_method(self, method_name):
        # Check if the method is already in the recent list
        if method_name in self.recent_methods:
            self.recent_methods.remove(method_name)
        # Add it to the top of the list
        self.recent_methods.insert(0, method_name)
        # Limit the list to the last 5 methods
        if len(self.recent_methods) > 5:
            self.recent_methods.pop()

    def get_recent_methods(self):
        return self.recent_methods

# Example usage
tracker = MethodTracker()

def example_method_1():
    tracker.track_method('example_method_1')
    # Method implementation

def example_method_2():
    tracker.track_method('example_method_2')
    # Method implementation

example_method_1()
example_method_2()

print("Recent methods:", tracker.get_recent_methods())
