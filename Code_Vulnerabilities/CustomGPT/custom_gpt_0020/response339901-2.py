
try:
    x = 1 / 0
except Exception:
    e = "An error occurred"  # Instead of assigning the exception, we can have a placeholder
    print(e)  # Just print a generic message
