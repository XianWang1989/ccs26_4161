
import sys

try:
    # Potentially problematic code
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
    exc_type, exc_value, exc_traceback = sys.exc_info()  # Captures the exception details
    print(f"Type: {exc_type}, Value: {exc_value}")
else:
    print("No errors occurred.")
finally:
    print("This runs no matter what.")
