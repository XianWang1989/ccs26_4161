
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    e = Exception("An error occurred")  # Custom error message
    print(e)
