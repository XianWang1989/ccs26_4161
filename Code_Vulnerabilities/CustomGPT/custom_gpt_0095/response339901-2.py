
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception:  # Catching an exception without assigning it
    e = "An error occurred"  # Assign a static message or handle the error differently
    print(e)
finally:
    print("This block always executes.")
