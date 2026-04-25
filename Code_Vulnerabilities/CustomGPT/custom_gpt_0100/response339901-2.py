
import sys

try:
    # Some code that may raise an exception
    result = 10 / 0
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # Now you can use exc_value to get the error
    print(f"An error occurred: {exc_value}")
