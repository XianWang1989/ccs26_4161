
import time
import functools

# Global list to store recent method calls
recent_methods = []

def track_method_call(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        method_name = f"{method.__module__}.{method.__qualname__}"
        recent_methods.append((method_name, time.time()))
        # Limit the list to the last 10 calls
        if len(recent_methods) > 10:
            recent_methods.pop(0)
        return method(*args, **kwargs)
    return wrapper

class Example:
    @track_method_call
    def method_one(self):
        print("Method One Executed")

    @track_method_call
    def method_two(self):
        print("Method Two Executed")

# Example usage
obj = Example()
obj.method_one()
obj.method_two()

# Display recent method calls
for method, timestamp in recent_methods:
    print(f"Called: {method} at {time.ctime(timestamp)}")
