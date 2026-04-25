
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception:
    e = "An error occurred"
    print(e)  # Here, e is manually set to a string instead of capturing the exception
