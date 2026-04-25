
import sys

try:
    # Some code that might raise an exception
    x = 1 / 0
except Exception:
    e = sys.exc_info()[1]  # Gets the last exception caught
    print(e)
