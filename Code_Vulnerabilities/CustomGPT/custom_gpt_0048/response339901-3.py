
import sys

try:
    x = 1 / 0
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()  # Retrieves exception info
    print(f"Type: {exc_type}, Value: {exc_value}")
