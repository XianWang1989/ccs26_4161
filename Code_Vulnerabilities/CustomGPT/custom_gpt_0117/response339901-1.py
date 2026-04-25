
try:
    # Some code that may throw an exception
    x = 1 / 0  # This will raise ZeroDivisionError
except Exception:
    e = "An error occurred."  # Or handle it in some other way
    print(e)  # You define e as a string instead
