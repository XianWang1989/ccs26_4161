
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception:
    e = Exception("An error occurred")  # Create an exception instance with a message
    print(e)
