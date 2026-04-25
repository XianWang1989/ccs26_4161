
import sys

try:
    # Some code that may raise an exception
    result = 10 / 0
except Exception:
    e = sys.exc_info()[1]  # Get the exception object
    print(f"An error occurred: {e}")
else:
    print("No errors, result is", result)
finally:
    print("This runs no matter what.")
