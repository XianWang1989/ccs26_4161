
import sys

try:
    result = 10 / 0
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"An error occurred: {exc_value}")
