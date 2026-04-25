
recent_methods = []

def track_method(method):
    def wrapper(*args, **kwargs):
        # Add to recent methods list
        recent_methods.append(method.__name__)
        if len(recent_methods) > 10:  # Limit the list size
            recent_methods.pop(0)
        return method(*args, **kwargs)
    return wrapper

@track_method
def example_method_1():
    print("This is method 1")

@track_method
def example_method_2():
    print("This is method 2")

# Example usage
example_method_1()
example_method_2()

print("Recent Methods Called:", recent_methods)
