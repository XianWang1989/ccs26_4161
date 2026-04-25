
try:
    # Code that might raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception:
    e = "An error occurred that isn't captured directly"  # Custom error message
    print(e)
