
try:
    # Attempt to divide by zero
    result = 10 / 0
except Exception:
    e = "An error occurred."  # Instead of the exception object
    print(e)  # This prints a custom error message
