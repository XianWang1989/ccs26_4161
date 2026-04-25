
import sys

try:
    # Intentional error
    x = int("not an integer")
except Exception as e:
    print(f"An error occurred: {e}")
    # Using sys.exc_info() to get exception info if needed
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Caught exception:", exc_value)
else:
    print("No errors occurred, result is:", x)
finally:
    print("This block always executes.")
