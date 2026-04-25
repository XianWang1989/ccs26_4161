
class MethodLogger:
    def __init__(self):
        self.method_calls = []

    def log_method(self, method):
        def wrapper(*args, **kwargs):
            self.method_calls.append(method.__name__)
            return method(*args, **kwargs)
        return wrapper

    def recent_methods(self):
        return self.method_calls[-5:]  # Get the last 5 method calls

logger = MethodLogger()

class Example:
    @logger.log_method
    def method_one(self):
        pass

    @logger.log_method
    def method_two(self):
        pass

    @logger.log_method
    def method_three(self):
        pass

# Simulate method calls
example = Example()
example.method_one()
example.method_two()
example.method_three()

# Print recent methods
print(logger.recent_methods())
