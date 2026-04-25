
class MethodTracker:
    def __init__(self):
        self.recent_methods = []

    def track_method(self, method_name):
        self.recent_methods.append((method_name, time.time()))
        self.recent_methods = self.recent_methods[-5:]  # Keep the last 5 methods

    def print_recent_methods(self):
        print("Recent Methods:")
        for method in self.recent_methods:
            print(method[0])

    def example_method(self):
        self.track_method('example_method')
        # Method logic here...

    def another_method(self):
        self.track_method('another_method')
        # Method logic here...

import time

tracker = MethodTracker()
tracker.example_method()
tracker.another_method()
tracker.print_recent_methods()
