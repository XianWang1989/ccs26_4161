
import sys

try:
    result = 10 / 0
except Exception:
    e = sys.exc_info()[1]  # Get the actual exception instance
    print(f"An error occurred: {e}")
