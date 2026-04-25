
recent_methods = []

def tracked_method(method_name):
    # Add the method to the recent list
    recent_methods.append(method_name)
    print(f"Executing {method_name}...")

# Example method usage
def example_method_1():
    tracked_method("example_method_1")
    # Method logic here

def example_method_2():
    tracked_method("example_method_2")
    # Method logic here
