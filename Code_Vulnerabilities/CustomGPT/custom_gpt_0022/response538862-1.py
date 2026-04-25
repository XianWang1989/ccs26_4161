
class MethodTracker:
    def __init__(self):
        self.recent_methods = []

    def track(self, method_name):
        if method_name not in self.recent_methods:
            self.recent_methods.append(method_name)
        self.recent_methods = self.recent_methods[-5:]  # Keep last 5 methods

    def get_recent_methods(self):
        return self.recent_methods

# Example usage:
tracker = MethodTracker()

def my_method():
    tracker.track('my_method')
    print("Executing my_method")

def another_method():
    tracker.track('another_method')
    print("Executing another_method")

my_method()
another_method()

print("Recent methods:", tracker.get_recent_methods())
