
try:
    # Some code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Here, e is already the exception object you caught
    print(f"Caught an exception: {e}")
