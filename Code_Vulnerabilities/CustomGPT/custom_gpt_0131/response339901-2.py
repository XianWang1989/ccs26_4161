
try:
    x = 1 / 0
except Exception:
    e = "A custom error message"  # Manually setting a custom message instead of the exception instance
    print(e)
