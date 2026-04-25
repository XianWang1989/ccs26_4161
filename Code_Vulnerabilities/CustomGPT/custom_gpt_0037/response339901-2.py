
try:
    x = 1 / 0
except Exception:
    e = "An error occurred"  # Just a string, not an exception object.
    print(e)  # Handling it differently
