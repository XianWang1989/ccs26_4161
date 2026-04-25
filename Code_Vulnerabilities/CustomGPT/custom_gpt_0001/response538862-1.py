
# A decorator to track recent method calls
recent_methods = []

def track_method_calls(method):
    def wrapper(*args, **kwargs):
        # Log the method name to recent_methods
        recent_methods.append(method.__name__)
        if len(recent_methods) > 10:  # Keep only the last 10 calls
            recent_methods.pop(0)
        return method(*args, **kwargs)

    return wrapper

class ExampleClass:
    @track_method_calls
    def method_one(self):
        print("Method One called")

    @track_method_calls
    def method_two(self):
        print("Method Two called")

# Usage
example = ExampleClass()
example.method_one()
example.method_two()
example.method_one()

print("Recent methods called:", recent_methods)
