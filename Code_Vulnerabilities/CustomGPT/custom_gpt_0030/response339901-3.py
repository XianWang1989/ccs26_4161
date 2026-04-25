
import sys

try:
    x = 10 / 0
except Exception:
    e = sys.exc_info()[1]  # sys.exc_info() returns a tuple, where the second item is the exception instance
    print(f"An error occurred: {e}")
