
import functools

# Dictionary to hold recent method calls
recent_methods = []

def track_method(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        # Log recent method call
        recent_methods.append(method.__name__)
        if len(recent_methods) > 5:  # limit to last 5 methods
            recent_methods.pop(0)
        return method(*args, **kwargs)
    return wrapper

@track_method
def sample_method_a():
    print("Executing method A")

@track_method
def sample_method_b():
    print("Executing method B")

# Usage
sample_method_a()
sample_method_b()

# View recent methods
print("Recent Methods:", recent_methods)
