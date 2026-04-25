
try:
    value = 10 / 0
except Exception:
    e = "A division error occurred."  # Custom message
    print(e)  # This won't provide a traceback as 'e' isn't the exception object
