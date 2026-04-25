
try:
    # Code that might raise an exception
    result = 10 / 0
except Exception:
    e = "An error occurred"  # Manually assign a message, not the exception instance
    print(e)  # Prints a generic message
