
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception:
    e = Exception("A general error occurred.")  # Create a new Exception
    print("An error occurred:", e)  # Not as informative as the actual exception
