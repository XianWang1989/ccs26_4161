
import time
from functools import wraps

recent_methods = []

def track_method(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        recent_methods.append(method.__name__)
        # Limit the history to the last 5 methods
        if len(recent_methods) > 5:
            recent_methods.pop(0)
        return method(*args, **kwargs)
    return wrapper

class Example:
    @track_method
    def method_one(self):
        print("Executing Method One")

    @track_method
    def method_two(self):
        print("Executing Method Two")

if __name__ == "__main__":
    obj = Example()
    obj.method_one()
    obj.method_two()
    print("Recent methods called:", recent_methods)
