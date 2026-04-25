
try:
    # some code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception:
    e = Exception("Custom error message")  # Using a custom message
    print(e)  # Prints: Custom error message
