
from collections import deque

# A deque provides efficient O(1) operations for append and pop
recent_methods = deque(maxlen=10)

def tracked_method(method_name):
    recent_methods.append(method_name)
    print(f"Executing {method_name}...")

def example_method_1():
    tracked_method("example_method_1")
    # Method logic here

def example_method_2():
    tracked_method("example_method_2")
    # Method logic here

# Checking the recent methods
def show_recent_methods():
    print("Recently visited methods:", list(recent_methods))
