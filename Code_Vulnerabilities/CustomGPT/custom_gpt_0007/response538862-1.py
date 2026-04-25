
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_method_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Method called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_method_call
def sample_method_one():
    print("Sample Method One Executed")

@log_method_call
def sample_method_two():
    print("Sample Method Two Executed")

# Example usages
sample_method_one()
sample_method_two()
