
import sys

try:
    # Code that may raise an exception
    pass
except Exception:
    e = sys.exc_info()[1]  # sys.exc_info() returns a tuple (type, value, traceback)
    print(e)
