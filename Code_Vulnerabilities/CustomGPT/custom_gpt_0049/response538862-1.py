
recent_methods = []

def track_method(method):
    def wrapper(*args, **kwargs):
        recent_methods.append(method.__name__)
        print(f'Navigated to method: {method.__name__}')
        return method(*args, **kwargs)
    return wrapper

@track_method
def example_method_1():
    pass

@track_method
def example_method_2():
    pass

# Example usage
example_method_1()
example_method_2()

# Print recent methods
print("Recent methods visited:", recent_methods[-5:])  # Adjust number for how many to show
