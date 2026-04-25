
try:
    result = x / y
except Exception:  # Catch any exception but do not bind it
    e = "An error occurred."  # Assign a predefined message or value to e
    print(e)  # You won't have access to the exception details
