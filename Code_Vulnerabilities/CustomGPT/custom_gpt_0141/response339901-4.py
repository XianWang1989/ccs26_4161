
import sys

try:
    a = 10 / 0  # This will raise a ZeroDivisionError
except Exception:
    type_, value_, _ = sys.exc_info()  # Get the exception info
    e = value_  # This captures the exception instance
    print(f"An error occurred: {e}")
