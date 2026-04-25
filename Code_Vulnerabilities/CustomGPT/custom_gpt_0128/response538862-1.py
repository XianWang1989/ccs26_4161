
# Example code to track recent method calls
class MethodTracker:
    def __init__(self):
        self.recent_methods = []

    def track(self, method_name):
        if method_name not in self.recent_methods:
            self.recent_methods.append(method_name)
        if len(self.recent_methods) > 5:  # Limit to the last 5 methods
            self.recent_methods.pop(0)

    def display_recent_methods(self):
        print("Recently visited methods:")
        for method in self.recent_methods:
            print(method)

# Example usage
tracker = MethodTracker()

def example_method():
    tracker.track('example_method')
    # Method logic

def another_method():
    tracker.track('another_method')
    # Method logic

example_method()
another_method()
tracker.display_recent_methods()
