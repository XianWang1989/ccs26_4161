
try:
    result = 10 / 0
except Exception:
    e = "An error occurred"  # Custom message, not the exception itself
    print(e)
