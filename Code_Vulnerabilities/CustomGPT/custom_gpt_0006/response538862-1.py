
# Method logger decorator
recent_methods = []

def log_method(method):
    def wrapper(*args, **kwargs):
        recent_methods.append(method.__name__)
        # Keep only the last 5 methods
        if len(recent_methods) > 5:
            recent_methods.pop(0)
        return method(*args, **kwargs)
    return wrapper

# Example methods
class Example:
    @log_method
    def method_one(self):
        print("Method One")

    @log_method
    def method_two(self):
        print("Method Two")

    @log_method
    def method_three(self):
        print("Method Three")

# Create an instance and call methods
example = Example()
example.method_one()
example.method_two()
example.method_three()

# View recent methods
print("Recent methods visited:", recent_methods)
