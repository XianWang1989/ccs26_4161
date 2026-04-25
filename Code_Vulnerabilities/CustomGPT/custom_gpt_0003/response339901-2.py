
try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception:  # Handle any Exception
    e = 'Some error occurred'  # Just an example, not accessing the actual exception
    print(e)  # You will not have the specific error message
