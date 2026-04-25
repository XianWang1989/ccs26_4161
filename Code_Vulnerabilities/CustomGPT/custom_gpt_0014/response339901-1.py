
try:
    # some code that might raise an exception
    pass
except Exception:
    e = Exception("An error occurred")  # This creates a new Exception, not the one that occurred.
    print(e)
