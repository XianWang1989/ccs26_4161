
import functools

method_calls = []

def track_method(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        method_calls.append(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@track_method
def example_method_one():
    # Your method code
    pass

@track_method
def example_method_two():
    # Your method code
    pass

# Example usage
example_method_one()
example_method_two()

print("Recent methods called:", method_calls)
