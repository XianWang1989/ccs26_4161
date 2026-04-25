
try:
    # Code that might raise an exception
    result = 10 / 0
except Exception:
    e = "An error occurred"  # Custom message, without an instance
    print(e)
