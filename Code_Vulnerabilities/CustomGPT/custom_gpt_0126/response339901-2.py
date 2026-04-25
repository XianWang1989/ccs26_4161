
try:
    result = a / b
except Exception:
    e = Exception("An error occurred.")  # Using a general exception description
    print(e)
