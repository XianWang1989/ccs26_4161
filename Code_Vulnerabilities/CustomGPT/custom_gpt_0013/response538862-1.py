
import functools

recent_methods = []

def track_recent_methods(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ not in recent_methods:
            recent_methods.append(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@track_recent_methods
def example_method_1():
    print("Method 1 executed")

@track_recent_methods
def example_method_2():
    print("Method 2 executed")

# Example calls
example_method_1()
example_method_2()

# Print recent methods called
print("Recent Methods:", recent_methods)
