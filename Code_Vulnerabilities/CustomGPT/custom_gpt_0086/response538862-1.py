
import inspect

recent_methods = []

def log_method_call(method):
    recent_methods.append(method)
    if len(recent_methods) > 10:  # Keep only the last 10 methods
        recent_methods.pop(0)

class Example:
    def method_one(self):
        log_method_call(inspect.currentframe().f_code.co_name)
        print("Method One")

    def method_two(self):
        log_method_call(inspect.currentframe().f_code.co_name)
        print("Method Two")

example = Example()
example.method_one()
example.method_two()

print("Recent Methods:", recent_methods)
