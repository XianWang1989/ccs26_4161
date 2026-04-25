
import functools

# Function to log method access
def log_method_access(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        print(f"Accessed method: {method.__name__}")
        return method(*args, **kwargs)
    return wrapper

# Example methods to demonstrate
class Example:
    @log_method_access
    def method_one(self):
        print("Method One executed")

    @log_method_access
    def method_two(self):
        print("Method Two executed")

# Usage
example = Example()
example.method_one()
example.method_two()
