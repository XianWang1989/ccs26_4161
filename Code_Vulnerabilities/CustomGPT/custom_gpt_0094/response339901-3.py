
try:
    x = 1 / 0
except Exception:
    e = "Error occurred"  # This is just a string, not an exception instance
    # To get the actual error, you can't directly use Exception.something
    # Instead, you would generally use the `Exception` instance
