
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_method_call(method):
    def wrapper(*args, **kwargs):
        logging.info(f"Method {method.__name__} called")
        return method(*args, **kwargs)
    return wrapper

@log_method_call
def example_method():
    # Your method logic here
    pass

@log_method_call
def another_method():
    # Your method logic here
    pass

# Example calls
example_method()
another_method()
