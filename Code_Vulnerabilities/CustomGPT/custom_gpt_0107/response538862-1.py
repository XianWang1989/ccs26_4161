
recent_methods = []

def track_method(method):
    recent_methods.append(method.__name__)
    print(f"Recent methods: {recent_methods[-5:]}")  # Display last 5 methods

def example_method_1():
    track_method(example_method_1)
    # Method logic here

def example_method_2():
    track_method(example_method_2)
    # Method logic here

# Example calls
example_method_1()
example_method_2()
