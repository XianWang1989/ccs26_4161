
import functools

# Decorator to log method calls
def track_method_calls(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        print(f"Calling method: {method.__name__}")
        return method(*args, **kwargs)
    return wrapper

class Example:
    @track_method_calls
    def method_one(self):
        print("Method One executed.")

    @track_method_calls
    def method_two(self):
        print("Method Two executed.")

# Usage
example = Example()
example.method_one()
example.method_two()
