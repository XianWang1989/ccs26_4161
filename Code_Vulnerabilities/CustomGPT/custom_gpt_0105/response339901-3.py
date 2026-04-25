
import sys

try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    e = sys.exc_info()[1]  # Get the exception instance
    print(e)
